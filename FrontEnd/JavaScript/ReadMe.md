
### 全局值属性
```
1. Infinity 无穷大
2. 
NaN === NaN;        // false
Number.NaN === NaN; // false
isNaN(NaN);         // true
isNaN(Number.NaN);  // true
3. undefined
一个没有被赋值的变量的类型是undefined。如果方法或者是语句中操作的变量没有被赋值，则会返回undefined
4. null
typeof null        // "object" (因为一些以前的原因而不是'null')
typeof undefined   // "undefined"
null === undefined // false
null  == undefined // true
null === null // true
null == null // true
!null //true
isNaN(1 + null) // false
isNaN(1 + undefined) // true
```

### 全局函数属性
```
1. eval() 函数会将传入的字符串当做 JavaScript 代码进行执行。
eval("2 + 2");             // returns 4
2. parseFloat()
3. parseInt()
4. decodeURI()
decodeURI("https://developer.mozilla.org/ru/docs/JavaScript_%D1%88%D0%B5%D0%BB%D0%BB%D1%8B");
// "https://developer.mozilla.org/ru/docs/JavaScript_шеллы"
encodeURI("http://username:password@www.example.com:80/path/to/file.php?foo=316&bar=this+has+spaces#anchor+ +你+ +好+[]+【】")
// http://username:password@www.example.com:80/path/to/file.php?foo=316&bar=this+has+spaces#anchor+%20+%E4%BD%A0+%20+%E5%A5%BD+%5B%5D+%E3%80%90%E3%80%91
```

### 基本类型
```
Object.length
值为1。
Object.prototype
可以为所有 Object 类型的对象添加属性。
1. assign()
const target = { a: 1, b: 2 };
const source = { b: 4, c: 5 };
const returnedTarget = Object.assign(target, source);
console.log(target);
// expected output: Object { a: 1, b: 4, c: 5 }
console.log(returnedTarget);
// expected output: Object { a: 1, b: 4, c: 5 }

```
###

### Array
let arr = [
    {
        label:"dogLabel",
        value:"dogValue"
    },
    {
        label:"pigLabel",
        value:"pigValue"
    },
    {
        label:"catLabel",
        value:"catValue"
    }
];

// 1. forEach() 遍历数组
arr.forEach((item, index) => {
    console.log(item,index);
});
/*
{ label: 'dogLabel', value: 'dogValue' } 0
{ label: 'pigLabel', value: 'pigValue' } 1
{ label: 'catLabel', value: 'catValue' } 2
*/

// 2. push() 添加元素到数组的末尾
let arr1 = arr.slice();
arr1.push({label:"mouseLabel", value:"mouseValue"});
console.log(arr1);
/*
[ { label: 'dogLabel', value: 'dogValue' },
  { label: 'pigLabel', value: 'pigValue' },
  { label: 'catLabel', value: 'catValue' },
  { label: 'mouseLabel', value: 'mouseValue' } ]
*/

// 3. pop() 删除数组末尾的元素
console.log(arr1.pop());
console.log(arr1);
/*
{ label: 'mouseLabel', value: 'mouseValue' }
[ { label: 'dogLabel', value: 'dogValue' },
  { label: 'pigLabel', value: 'pigValue' },
  { label: 'catLabel', value: 'catValue' } ]
*/

// 4. shift()/unshift() 删除数组最前面（头部）的元素
let arr2 = arr.slice();
console.log(arr2.shift());
console.log(arr2);
/*
{ label: 'dogLabel', value: 'dogValue' }
[ { label: 'pigLabel', value: 'pigValue' },
  { label: 'catLabel', value: 'catValue' } ]
*/
arr2.unshift({ label: 'monkeyLabel', value: 'monkeyValue' })
console.log(arr2);
/*
[ { label: 'monkeyLabel', value: 'monkeyValue' },
  { label: 'pigLabel', value: 'pigValue' },
  { label: 'catLabel', value: 'catValue' } ]
*/

// 5. indexOf() 找出某个元素在数组中的索引
let arr3 = arr.slice();
let pos = arr3.indexOf({label: 'pigLabel', value: 'pigValue'});
console.log(pos);
// -1 只支持字符串数组

// 6. 通过索引删除某个元素
let removeItem = arr3.splice(pos, 1);
console.log(removeItem);
console.log(arr3);
/*
[ { label: 'catLabel', value: 'catValue' } ]
[ { label: 'dogLabel', value: 'dogValue' },
  { label: 'pigLabel', value: 'pigValue' } ]
*/

// 7. slice() 复制一个数组

// 8. splice()
var months = ['Jan', 'March', 'April', 'June'];
months.splice(1, 0, 'Feb');
// inserts at 1st index position
console.log(months);
// expected output: Array ['Jan', 'Feb', 'March', 'April', 'June']
months.splice(4, 1, 'May');
// replaces 1 element at 4th index
console.log(months);
// expected output: Array ['Jan', 'Feb', 'March', 'April', 'May']

// 9.sort() 默认排序顺序是根据字符串Unicode码点。该方法会改变原数组。
// reverse() 方法将数组中元素的位置颠倒,并返回该数组。该方法会改变原数组。
var array1 = [1, 30, 4, 21, 100000];
array1.sort();
console.log(array1);
// expected output: Array [1, 100000, 21, 30, 4]

// 10. some() 方法测试是否至少有一个元素通过由提供的函数实现的测试。
var array = [1, 2, 3, 4, 5];
var even = function(element) {
  // checks whether an element is even
  return element % 2 === 0;
};
console.log(array.some(even));
// expected output: true

// 11. reduce() 方法对数组中的每个元素执行一个由您提供的reducer函数(升序执行)，将其结果汇总为单个返回值。
const array1 = [1, 2, 3, 4];
const reducer = (accumulator, currentValue) => accumulator + currentValue;
// 1 + 2 + 3 + 4
console.log(array1.reduce(reducer));
// expected output: 10
// 5 + 1 + 2 + 3 + 4
console.log(array1.reduce(reducer, 5));
// expected output: 15

// 12. map() 方法创建一个新数组，其结果是该数组中的每个元素都调用一个提供的函数后返回的结果。
let output12 = arr.map((item)=>{
    if (item.label === "dogLabel"){
            return item;
    }
})
console.log(output12);
// expected output: 
Array [Object { label: "dogLabel", value: "dogValue" }, undefined, undefined]

// 13. lastIndexOf() 方法返回指定元素（也即有效的 JavaScript 值或变量）在数组中的最后一个的索引，如果不存在则返回 -1。从数组的后面向前查找，从 fromIndex 处开始。lastIndexOf 使用严格相等（strict equality，即 ===）比较 searchElement 和数组中的元素
indexOf()方法返回在数组中可以找到一个给定元素的第一个索引，如果不存在，则返回-1。
var animals = ['Dodo', 'Tiger', 'Penguin', 'Dodo'];
console.log(animals.lastIndexOf('Dodo'));
// expected output: 3
console.log(animals.lastIndexOf('Tiger'));
// expected output: 1

// 14. join() 方法将一个数组（或一个类数组对象）的所有元素连接成一个字符串并返回这个字符串。如果数组只有一个项目，那么将返回该项目而不使用分隔符。
var elements = ['Fire', 'Wind', 'Rain'];
console.log(elements.join());
// expected output: "Fire,Wind,Rain"
console.log(elements.join(''));
// expected output: "FireWindRain"
console.log(elements.join('-'));
// expected output: "Fire-Wind-Rain"

// 15. includes() 方法用来判断一个数组是否包含一个指定的值，根据情况，如果包含则返回 true，否则返回false。

// 16. forEach((item)=>{}) forEach() 方法对数组的每个元素执行一次提供的函数。

// 17.flat() 方法会按照一个可指定的深度递归遍历数组，并将所有元素与遍历到的子数组中的元素合并为一个新数组返回。
var arr1 = [1, 2, [3, 4]];
arr1.flat(); 
// [1, 2, 3, 4]
var arr2 = [1, 2, [3, 4, [5, 6]]];
arr2.flat();
// [1, 2, 3, 4, [5, 6]]
var arr3 = [1, 2, [3, 4, [5, 6]]];
arr3.flat(2);
// [1, 2, 3, 4, 5, 6]
//使用 Infinity 作为深度，展开任意深度的嵌套数组
arr3.flat(Infinity); 
// [1, 2, 3, 4, 5, 6]
flat() 方法会移除数组中的空项:
var arr4 = [1, 2, , 4, 5];
arr4.flat();
// [1, 2, 4, 5]

// 18. findIndex()方法返回数组中满足提供的测试函数的第一个元素的索引。否则返回-1。
var array1 = [5, 12, 8, 130, 44];
function isLargeNumber(element) {
  return element > 13;
}
console.log(array1.findIndex(isLargeNumber));
// expected output: 3

// 19.  find() 方法返回数组中满足提供的测试函数的第一个元素的值。否则返回 undefined。
var array1 = [5, 12, 8, 130, 44];
var found = array1.find(function(element) {
  return element > 10;
});
console.log(found);
// expected output: 12

// 20. filter() 方法创建一个新数组, 其包含通过所提供函数实现的测试的所有元素。 
var words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];
const result = words.filter(word => word.length > 6);
console.log(result);
// expected output: Array ["exuberant", "destruction", "present"]

// 21. fill() 方法用一个固定值填充一个数组中从起始索引到终止索引内的全部元素。不包括终止索引。
var array1 = [1, 2, 3, 4];
// fill with 0 from position 2 until position 4
console.log(array1.fill(0, 2, 4));
// expected output: [1, 2, 0, 0]
// fill with 5 from position 1
console.log(array1.fill(5, 1));
// expected output: [1, 5, 5, 5]
console.log(array1.fill(6));
// expected output: [6, 6, 6, 6]

// 22. every() 方法测试数组的所有元素是否都通过了指定函数的测试。
function isBelowThreshold(currentValue) {
  return currentValue < 40;
}
var array1 = [1, 30, 39, 29, 10, 13];
console.log(array1.every(isBelowThreshold));
// expected output: true

// 23. entries() 方法返回一个新的Array Iterator对象，该对象包含数组中每个索引的键/值对。
var array1 = ['a', 'b', 'c'];
var iterator1 = array1.entries();
console.log(iterator1.next().value);
// expected output: Array [0, "a"]
console.log(iterator1.next().value);
// expected output: Array [1, "b"]

// 24. copyWithin() 方法浅复制数组的一部分到同一数组中的另一个位置，并返回它，而不修改其大小。
var array1 = ['a', 'b', 'c', 'd', 'e'];
// copy to index 0 the element at index 3
console.log(array1.copyWithin(0, 3, 4));
// expected output: Array ["d", "b", "c", "d", "e"]
// copy to index 1 all elements from index 3 to the end
console.log(array1.copyWithin(1, 3));
// expected output: Array ["d", "d", "e", "d", "e"]

// 25. concat() 方法用于合并两个或多个数组。此方法不会更改现有数组，而是返回一个新数组。
var array1 = ['a', 'b', 'c'];
var array2 = ['d', 'e', 'f'];
console.log(array1.concat(array2));
// expected output: Array ["a", "b", "c", "d", "e", "f"]

// 26. Array.isArray() 用于确定传递的值是否是一个 Array。
Array.isArray([1, 2, 3]);  
// true
Array.isArray({foo: 123}); 
// false
Array.isArray("foobar");   
// false
Array.isArray(undefined);  
// false

// 27. Array.from() 方法从一个类似数组或可迭代对象中创建一个新的数组实例。
console.log(Array.from('foo'));
// expected output: Array ["f", "o", "o"]
console.log(Array.from([1, 2, 3], x => x + x));
// expected output: Array [2, 4, 6]

###