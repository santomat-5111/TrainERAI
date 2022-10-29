var age = document.getElementById("age");
var height = document.getElementById("height");
var weight = document.getElementById("weight");
var male = document.getElementById("m");
var female = document.getElementById("f");
var form = document.getElementById("form");
function validateForm() {
  if (
    age.value == "" ||
    height.value == "" ||
    weight.value == "" ||
    (male.checked == false && female.checked == false)
  ) {
    alert("All fields are required!");
    document.getElementById("submit").removeEventListener("click", countBmi);
  } else {
    countBmi();
  }
}
document.getElementById("submit").addEventListener("click", validateForm);
function countBmi() {
  var p = [age.value, height.value, weight.value];
  var gender = "";
  var bmr;
  if (male.checked) {
    p.push("male");
    gender = "male";
  } else if (female.checked) {
    p.push("female");
    gender = "female";

  }
  form.reset();
  var bmi = Number(p[2]) / (((Number(p[1]) / 100) * Number(p[1])) / 100);
  var result = "";
  var suggested_calories = "";
  if(gender == "male")
    if (bmi < 18.5) {
      result = "Underweight";
      bmr = 66.47 + (13.75*pi[2]) + (5.003*pi[1]) - (6.755*pi[0]);
      suggested_calories = bmr *1.55;
    } else if (18.5 <= bmi && bmi <= 24.9) {
      result = "Healthy";
      bmr = 66.47 + (13.75*pi[2]) + (5.003*pi[1]) - (6.755*pi[0]);
      suggested_calories = bmr *1.55;
    } else if (25 <= bmi && bmi <= 29.9) {
      result = "Overweight";
      bmr = 66.47 + (13.75*pi[2]) + (5.003*pi[1]) - (6.755*pi[0]);
      suggested_calories = bmr *1.55;
    } else if (30 <= bmi && bmi <= 34.9) {
      result = "Obese";
      bmr = 66.47 + (13.75*pi[2]) + (5.003*pi[1]) - (6.755*pi[0]);
      suggested_calories = bmr *1.55;
    } else if (35 <= bmi) {
      result = "Extremely obese";
      bmr = 66.47 + (13.75*pi[2]) + (5.003*pi[1]) - (6.755*pi[0]);
      suggested_calories = bmr *1.55;
      
    }

  else if(gender == "female")
    if (bmi < 18.5) {
      result = "Underweight";
      bmr = 655.1 + (9.563*pi[2]) + (1.850*pi[1]) - (4.676*pi[0]);
      suggested_calories = bmr *1.55;
    } else if (18.5 <= bmi && bmi <= 24.9) {
      result = "Healthy";
      bmr = 655.1 + (9.563*pi[2]) + (1.850*pi[1]) - (4.676*pi[0]);
      suggested_calories = bmr *1.55;
    } else if (25 <= bmi && bmi <= 29.9) {
      result = "Overweight";
      bmr = 655.1 + (9.563*pi[2]) + (1.850*pi[1]) - (4.676*pi[0]);
      suggested_calories = bmr *1.55;
    } else if (30 <= bmi && bmi <= 34.9) {
      result = "Obese";
      bmr = 655.1 + (9.563*pi[2]) + (1.850*pi[1]) - (4.676*pi[0]);
      suggested_calories = bmr *1.55;
    } else if (35 <= bmi) {
      result = "Extremely obese";
      bmr = 655.1 + (9.563*pi[2]) + (1.850*pi[1]) - (4.676*pi[0]);
      suggested_calories = bmr *1.55;

    }  
  var link="";
  if (result == "Underweight") {
    link = "workout_planner_underweight.html";
  } else if (result == "Healthy") {
    link = "workout_planner_normal.html";;
  } else if (result == "Overweight") {
    link = "workout_planner_overweight.html";
  } else if (result == "Obese") {
    link = "workout_planner_obese.html";
  }

  document.getElementById("myAnchor").href = link;


  var h1 = document.createElement("h1");
  var h2 = document.createElement("h2");
  var t = document.createTextNode(result);
  var b = document.createTextNode("BMI: ");
  var r = document.createTextNode(parseFloat(bmi).toFixed(2));
  var s = document.createTextNode("Suggested Calories: ");
  var c = document.createTextNode(parseFloat(suggested_calories).toFixed(2));

  h1.appendChild(t);
  h2.appendChild(b);
  h2.appendChild(r);
  h2.appendChild(s);
  h2.appendChild(c);
  
  document.body.appendChild(h1);
  document.body.appendChild(h2);
  document.body.appendChild(h2);

  document.getElementById("submit").removeEventListener("click", countBmi);
  document.getElementById("submit").removeEventListener("click", validateForm);
}
document.getElementById("submit").addEventListener("click", countBmi);
