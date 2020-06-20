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

console.log(arr.includes({
    label:"catLabel",
    value:"catValue"
}))