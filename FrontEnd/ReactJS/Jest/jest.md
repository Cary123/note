# <center>jest + enzyme 的用法</center>
## Table of Contents
- [VSCode Debug](#VSCode-Debug)
- [配置package.json](#配置package.json)
- [Jest知识](#Jest知识)
- [案例](#案例)

- [jest官网](https://jestjs.io/docs/en/api)
- [enzyme官网](https://airbnb.io/enzyme/)

## VSCodeDebug

下载Jest插件，[配置VSCode](https://jestjs.io/docs/en/troubleshooting.html#debugging-in-vs-code) (.vscode/launch.json)

```json
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "type": "node",
            "name": "vscode-jest-tests",
            "request": "launch",
            "runtimeExecutable": "${workspaceRoot}/node_modules/.bin/react-scripts",
            "port": 9230,
            "runtimeArgs": [
                "--inspect-brk=9230",
                "--inspect-brk",
                "test"
              ],
            "args": [
                "--runInBand",
                "--no-cache",
                "--env=jsdom"
            ],
            "cwd": "${workspaceFolder}",
            "console": "integratedTerminal",
            "internalConsoleOptions": "neverOpen",
            "program": "${workspaceFolder}/node_modules/jest/bin/jest"
        }
    ]
}
```

## 配置package.json

```json
"scripts": {
"debugger": "react-scripts --inspect-brk test --runInBand --env=jsdom"
 }
```

## Jest知识

Jest的API更多着力于定义测试、断言、mock库

### 定义测试：
* describe: 定义一个测试套件（test suite）
* it: 定义一个测试（test）
* beforeEach: 定义一个回调函数在每个测试之前执行
* expect: 执行一个断言
* jest.fn(): 创造一个mock函数

### 一些用于断言的方法：
* toEqual: 验证两个值是否相同
* toBe: 验证两个值是否 === 完全相等
* toHaveLength：验证长度
* toBeDefined: 验证一个值是否被定义
* toContain: 验证一个list中是否包含某一项
* toBeCalled: 验证一个mock函数是否被调用
* toBeCalledWith: 验证一个mock函数是否被传入指定的参数被调用

### 一些用于mock的方法:
* mockImplementation: 提供mock函数的执行
* mockReturnValue: mock函数被调用返回一个值
* Enzyme的API更多着重于渲染react组件和从dom树种检索指定的节点

### 下面是三种渲染组件的方法：
* shallow: 会渲染至虚拟dom，不会返回真实的dom节点，大幅提升测试性能
* mount: 实现Full Rendering 比如说当我们需要对DOM API交互或者你需要测试组件的整个生命周期的时候，需要使用这个方法。
* render: 渲染出最终的html，然后利用这个html结构来进行分析处理

### 一些被渲染的组件检索节点的方法:
* find: 通过匹配选择器来检索节点
* some: 当至少有一个节点匹配选择器是返回true
* first: 返回集合的第一个节点
* at: 返回集合的第n个节点
* html: 获取节点的HTML结构
* text: 获取节点的文本

### 一些用于组件交互的方法：
* simulate: 模拟一个事件
* setProps: 设置props
* setState: 设置state
* props(key): 用于检索组件的props
* state(key): 用于检索组件的state


## 案例

### 使用jest.fn()对方法进行mock
```javascript
import Component from "../component";
const mock_fn = jest.fn();
const wrapper = mount(
    < Component ></Component>
);
```

### 使用enzyme的instance()方法将组件内的fn()方法替换为mock_fn()
wrapper.instance().fn = mock_fn; 
```javascript
import store from "../store";
spy_storeFn = jest.spyOn(store, "storeFn");
//使用reactWapper.instance()获取组件内部方法并进行mock
category_mount.instance().clickTextToCenter = mock_clickTextToCenter;
```

### 关于enzyme
```
render采用的是第三方库Cheerio的渲染，渲染结果是普通的html结构，对于snapshot使用render比较合适。
mount和shallow对组件的渲染结果不是html的dom树，而是react树，如果你chrome装了react devtool插件，他的渲染结果就是react devtool tab下查看的组件结构，而render的结果是element tab下查看的结果。这些只是渲染结果上的差别，更大的差别是shallow和mount的渲染结果是个被封装的ReactWrapper，可以进行多种操作，譬如find()、parents()、children()等选择器进行元素查找；state()、props()进行数据查找，setState()、setprops()操作数据；simulate()模拟事件触发等。
shallow只渲染当前组件，只能能对当前组件做断言；mount会渲染当前组件以及所有子组件，对所有子组件也可以做上述操作。一般交互测试都会关心到子组件，使用的都是mount。但是mount耗时更长，内存占用的更多，如果没必要操作和断言子组件，可以使用shallow。
```

## 文件引入（xxx.test.js）
```javascript
//list_guide.test.js
import React from "react";  // 必须引入react
import "../assets/configs/global_configs"; //引入全局的依赖文件以免npm run test时报错
import { ns } from "../src/configs/configs"; //引入组件依赖的配置文件
import store from "../src/pages/list/store";  //可以引入store，支持对store进行操作
import mockList from "../__mocks__/list"; //引入mock数据
import { shallow, render } from "enzyme";  //引入enzyme的渲染方法
import Guide from "../src/pages/list/guide";  //引入待测的组件
import toJson from "enzyme-to-json"; // 引入enzyme-to-json为快照提供了json的组件格式
//import { BrowserRouter } from "react-router-dom"; 
//对于使用<Route>包裹的组件需要进入BrowserRouter,
//否则报错“You should not use <Route> or withRouter() outside a <Router>”

describe("pages/list/guide",()=>{
  const { setValue } = store;

  it("should render without throwing an error",()=>{
    setValue("guide_visible", true);
    const Guide_render = render(
      <Guide store ={store}/> //直接使用store将引入的store传给待测组件
    );
    expect(toJson(Guide_render)).toMatchSnapshot();  //生成快照

    const Guide_shallow = shallow(
      <Guide store ={store}/>
    );
    expect(Guide_shallow.hasClass("hide")).toEqual(false);
    Guide_shallow.find(`.${ns}-guide`).at(0).simulate("click");
    expect(Guide_shallow.hasClass("hide")).toEqual(true);
  });
});
```

### 快照测试
- 快照可以测试到组件的渲染结果是否与上一次生成的快照一致；
toMatchSnapshot方法会帮助我们对比这次将要生成的结构与上次的区别；
快照测试是最简单且收益很快的测试方法，建议每个组件都进行快照测试。
```javascript
// list_category.test.js
import "../assets/configs/global_configs";
import React from "react";
import store from "../src/pages/list/store";
import { shallow, mount, render } from "enzyme";
import Category from "../src/pages/list/category";
import { ns } from "../src/configs/configs";
import { BrowserRouter } from "react-router-dom"; 
import mockList from "../__mocks__/list"; 
import toJson from "enzyme-to-json"; 

describe("pages/list/category", () => {
  //执行每个用例之前清除掉所有mock
  beforeEach(()=>{
    jest.clearAllMocks();
  });
  const { setValue } = store;
  
  it("type = thirdparty_web", () => {
    setValue("category_data", mockList.category_data.thirdparty_web);
    //使用render进行快照测试，直接展示的是html树
    const category_render = render(
      <BrowserRouter>
        <Category store={store}></Category>
      </BrowserRouter>
    );
    
    //生成快照，如安装了VScode的jest插件，这里会显示view snapshot,点击可查看快照
    //toJson()将reactWrapper转化为json格式用来生成快照
    expect(toJson(category_render)).toMatchSnapshot();    
    
    //使用mount进行交互测试
    const category_mount = mount(
      <BrowserRouter>
        <Category store={store}></Category>
      </BrowserRouter>
    );
    expect(category_mount.find("Router span").text()).toEqual("益智游戏");
    expect(category_mount.find(".swiper-slide").at(1).text()).toEqual("推荐书籍");
  });
  
 
});
```

### 交互测试
- 主要利用enzyme的simulate()方法来模拟事件，通过触发事件绑定函数，模拟事件的触发。触发事件后，判断props上特定函数是否被调用，传参是否正确；组件状态是否发生预料之中的修改；store中的值是否按照预期变化；某个dom节点是否存在是否符合期望。
```javascript
// list_category.test.js
import "../assets/configs/global_configs";
import React from "react";
import store from "../src/pages/list/store";
import { shallow, mount, render } from "enzyme";
import Category from "../src/pages/list/category";
import { ns } from "../src/configs/configs";
import { BrowserRouter } from "react-router-dom";
import mockList from "../__mocks__/list";
import toJson from "enzyme-to-json"; 

describe("pages/list/category", () => {
  //执行每个用例之前清除掉所有mock
  beforeEach(()=>{
    jest.clearAllMocks();
  });
  const { setValue } = store;
  
  ...

  it("no dropdown", () => {
    setValue("category_data", mockList.category_data.no_dropdown);
    const category_render = render(
      < Category store={store}></Category>
    );
    expect(toJson(category_render)).toMatchSnapshot(); // 生成快照
    
    const category_mount = mount(
      < Category store={store}></Category>
    );
    expect(category_mount.find(`.${ns}-swiper-container .swiper-slide`).map(node => node.text()))
      .toEqual(["每月推荐", "中国影片", "欧洲电影", "亚洲电影", "国际影院", "儿童电影"]);

    const 
    //使用jest.fn()对方法进行mock
    mock_clickTextToCenter = jest.fn(),
    //使用jest.spyOn()模拟跟踪某个类的方法的调用
    spy_showList = jest.spyOn(store, "showList");
    //使用reactWapper.instance()获取组件内部方法并进行mock
    category_mount.instance().clickTextToCenter = mock_clickTextToCenter;
    //使用simulate()触发click事件
    category_mount.find(".swiper-slide").at(3).simulate("click");
    //检测模拟的Category组件内部的clickTextToCenter方法是否调用并且参数是3
    expect(mock_clickTextToCenter).toHaveBeenCalledWith(3);
    //检测store中的current_type是否已经变为good_page
    expect(store.current_type).toEqual("good_page");
      //检测store中的current_id是否已经变为30065936895
    expect(store.current_id).toEqual(30065936895);
    //检测模拟的store中的showList方法是否被调用并且参数是good_page，good_page，1
    expect(spy_showList).toHaveBeenCalledWith("good_page", good_page, 1);
  });
  
});
```

### 例子1
```javascript
import React, { PureComponent } from 'react';
import { mount, ReactWrapper, render } from 'enzyme';
import YearPicker from '..';

import moment from 'moment';

class YearPickerDemo extends React.Component {
  state = {
    cleared: false,
    value: moment().format('YYYY'),
  };

  render() {
    return (
      <YearPicker
        showTime
        format="YYYY"
        onChange={this.onChange}
        defaultValue={moment('2015/01/01', 'YYYY')}
      />
    );
  }
}

//这里定义了3个测试内容

//测试默认值，即检查输入框的值是否为默认值
//测试清除按钮是否可用，通过模拟点击清除按钮，测试是否能按照预期清除输入框内填充的默认值
//测试设置值，点击输入框，弹出选择框，选择值，检查输入框中的值是否为选择的值

describe('DatePicker', () => {
  it('default value', () => {
    const wrapper = mount(<YearPickerDemo/>);
    expect(wrapper.find('.ant-calendar-picker-input').getDOMNode().value).toBe('2015');
  });

  it('clear value', () => {
    const wrapper = mount(<YearPickerDemo/>);
    wrapper.find('.ant-calendar-picker-clear').hostNodes().simulate('click');
    expect(wrapper.find('.ant-calendar-picker-input').getDOMNode().value).toBe('');
  });

  it('set value in calendar', () => {
    const wrapper = mount(<YearPickerDemo/>);
    wrapper.find('.ant-calendar-picker-input').simulate('click');
    const triggerWrapper = mount(wrapper.find('Trigger').instance().getComponent());
    triggerWrapper.find('[title="2018"]').simulate('click');
    expect(wrapper.find('.ant-calendar-picker-input').getDOMNode().value).toBe('2018');
  });
});
```
