const date = new Date();
const selectedDate = new Date();

const renderCalendar = () => {
    
const monthDays = document.querySelector('.days');

const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();

const prevLastDay = new Date(date.getFullYear(), date.getMonth(), 0).getDate();

const convertDays = (day) => {

   return (day === 0) ? 6 : day - 1
}

const firstDayIndex = convertDays(new Date(date.getFullYear(), date.getMonth(), 1).getDay());

const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

document.querySelector('.date h1').innerHTML = months[date.getMonth()];

document.querySelector('.date p').innerHTML = selectedDate.toDateString();


let days = "";
let totalDays = 0;

for(let x = firstDayIndex; x > 0; x--){
    days += `<div class="prev-date">${prevLastDay - x + 1}</div>`
    totalDays += 1;
}

for(let i = 1; i <= lastDay; i++){
    let currentDate = date
    currentDate.setDate(i)
    currentDate = currentDate.toDateString()
    let workout = JSON.parse(localStorage.getItem(currentDate))


    if(i === new Date().getDate() && date.getMonth() === new Date().getMonth() && date.getFullYear() === new Date().getFullYear()){

        if(date.toString() === selectedDate.toString()){
            days += `<div class="selectedToday">${i}</div>`
        }
        else{
            days += `<div today class="today">${i}</div>`
        }
        totalDays += 1;
    }
    else if(i === selectedDate.getDate() && date.getMonth() === selectedDate.getMonth() && date.getFullYear() === selectedDate.getFullYear()){
        if(workout !== null){
            days += `<div selectedSavedDay class="selectedSavedDay">${i}</div>`
        }else{
            days += `<div selectedDay class="selectedDay">${i}</div>` 
        }
        totalDays += 1;
    }
    else{
        if(workout !== null){
            days += `<div savedDay class="savedDay">${i}</div>`  
        }else{
            days += `<div day>${i}</div>`  
        }
        totalDays += 1;
    }
}

for(let i = 1; totalDays < 42; i++){
    days += `<div class="next-date">${i}</div>`
    totalDays += 1;
}
monthDays.innerHTML = days;

document.querySelectorAll('[day],[today],[savedDay]').forEach(day => {
    day.addEventListener('click', () => {
        selectedDate.setMonth(date.getMonth());
        selectedDate.setFullYear(date.getFullYear());
        selectedDate.setDate(day.innerHTML);
        renderCalendar();
    })
})

let workout = JSON.parse(localStorage.getItem(selectedDate.toDateString()))

if(workout === null){
    document.getElementById("set1").value = ""
    document.getElementById("rep1").value = ""
    document.getElementById("set2").value = ""
    document.getElementById("rep2").value = ""
    document.getElementById("set3").value = ""
    document.getElementById("rep3").value = ""
}else{
    document.getElementById("set1").value = workout.workout1.name
    document.getElementById("rep1").value = workout.workout1.weight
    document.getElementById("set2").value = workout.workout2.name
    document.getElementById("rep2").value = workout.workout2.weight
    document.getElementById("set3").value = workout.workout3.name
    document.getElementById("rep3").value = workout.workout3.weight 
}


}

document.querySelector('.prev').addEventListener('click', () => {
    date.setDate(1);
    date.setMonth(date.getMonth()-1);
    renderCalendar();
});

document.querySelector('.next').addEventListener('click', () =>{
    date.setDate(1);
    date.setMonth(date.getMonth()+1);
    renderCalendar();
});

renderCalendar();

document.querySelector('.Save').addEventListener('click', () => {
    saveWorkout();
})

document.querySelector('.Delete').addEventListener('click', () => {
    clearWorkout();
})

const saveWorkout = () => {

const workout = {
    date: selectedDate,
    workout1: {
        name: document.getElementById("set1").value,
        weight: document.getElementById("rep1").value,
    },
    workout2: {
        name: document.getElementById("set2").value,
        weight: document.getElementById("rep2").value,
    },
    workout3: {
        name: document.getElementById("set3").value,
        weight: document.getElementById("rep3").value,
    }
};

localStorage.setItem(selectedDate.toDateString(), JSON.stringify(workout, null, 2));    

renderCalendar();
};

const clearWorkout = () => {
    localStorage.removeItem(selectedDate.toDateString());
    document.getElementById("set1").value = ""
    document.getElementById("rep1").value = ""
    document.getElementById("set2").value = ""
    document.getElementById("rep2").value = ""
    document.getElementById("set3").value = ""
    document.getElementById("rep3").value = ""
    renderCalendar();
}


