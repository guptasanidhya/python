function usersinput(){
const pregnancies1=document.querySelector('#pregnancies');
const glucose1=document.querySelector('#glucose');
const diastolic1=document.querySelector('#diastolic');
const triceps1=document.querySelector('#triceps');
const insulin1=document.querySelector('#insulin');
const bmi1=document.querySelector('#bmi');
const dpf1=document.querySelector('#dpf');
const age1=document.querySelector('#age');
const userList=document.querySelector('#users');

const li = document.createElement('li');
//add text node with input value
    // li.innerHTML = `<strong>${nameInput.value}</strong>e: ${emailInput.value}`;
li.appendChild(document.createTextNode(`pregnancies:${pregnancies1.value}, glucose:${glucose1.value}, diastolic:${diastolic1.value}, triceps:${triceps1.value}, insulin:${insulin1.value}, bmi:${bmi1.value}, dpf:${dpf1.value}, age:${age1.value}`));
    // Append to ul
    userList.appendChild(li);
}