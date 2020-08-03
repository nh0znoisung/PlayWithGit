let baseSalary = 30_000;
let overtime = 10;
let rate = 20;

function getWage(baseSalary, overtime, rate) {
    return baseSalary + (overtime * rate)
}

let employee = {
    baseSalary : 30_000,
    overtime : 10,
    rate : 20,
    getWage : function(){
        return this.baseSalary + (this.overtime * this.rate);
    }
}
console.log(employee.getWage());
//object
// const circle = {
//     radius :1,
//     location:{
//         x:1,
//         y:1
//     },
//     draw:function(){
//         console.log('draw')
//     }
// }

//Factory function
function createCircle(radius){
    return {
        radius: radius,
        location:{
            x : 1,
            y : 1
        },
        draw: function (){
            console.log('draw')
        }
    };
}

// const circle = createCircle(1)

// COnstructor Function
function Circle(radius){
    console.log('this',this);
    this.radius = radius;
    this.draw = function(){
        console.log('draw');
    }
}

const circle = new Circle(10)
circle.location = {x:1}
const propertyName = 'location'
circle[propertyName] = {x:1}

for(let key in circle){
    console.log(key);
}

function power(base , exponent){
    if(exponent === 0){
        return 1;
    }else{
        
        if(exponent%2 == 0){ 
            let x =  power(base, exponent/2);
            return x*x;
        }else{
            let x =  power(base, exponent/2);
            return base*x*x;
        }
    }
}
console.log(power(2,3))