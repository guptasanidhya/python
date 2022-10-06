
//#########################################################################################################################
//the checks start

var counter = 0;
$('.images img').each(function(i) {
   if (i == 0) {
       counter = 0;
   } else {
       counter++;
   }
   if (counter < 18) {
       $(this).addClass('show');
   } else {
     $(this).addClass('hide');
   }
});


function shuffleRandomLogos(remove, add) {
  const logo = $("."+remove).toArray();
  //const logo = $('.images'+remove).toArray();
  //const logo = $(".images img").toArray();
  const logoLength = logo.length;
  const randomNum = Math.floor(Math.random()*logoLength);
  const randomLogo = logo[randomNum];
  $(randomLogo).removeClass(remove);
  $(randomLogo).addClass(add);
}

window.setInterval(function(){
  // remove a cat
  shuffleRandomLogos("show", "hide");
  // display a cat
  shuffleRandomLogos("hide", "show");
}, 600);

//#####################################################################################################################
//checks end


//result pool
//#####################################################################################################################
//#####################################################################################################################
var curl = window.location.href;
if(curl=='http://127.0.0.1:5000/predict'){
    window.onload = function () {
        console.log("loading map");
        loadmap();
        }}
function loadmap(){ 
var iframe = document.createElement('iframe');
iframe.width = "750px";
iframe.height = "550px";
iframe.id = "iframe";
iframe.allowfullscreen="";
iframe.loading="lazy";
iframe.referrerpolicy="no-referrer-when-downgrade"
document.getElementById("headIntro").innerHTML = "Diabetes Center Nearby";
document.getElementById("small").innerHTML="Its always best to consult a physician or doctor nearby you";
document.getElementById("p1").innerHTML="";
document.getElementById("p2").innerHTML="";
document.getElementById("p3").innerHTML="";
document.getElementById("p1").appendChild(iframe);
iframe.src="https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d58893.09290108873!2d75.84210120193823!3d22.697806756135595!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1sdiabetes%20center%20near%20me!5e0!3m2!1sen!2sin!4v1657522313247!5m2!1sen!2sin";
// var btndiv = document.getElementById("button2");
// document.getElementById("introSection").removeChild(btndiv);
$("#introSection button").remove();
}

 //
///////////////////////////////////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function pregnancies() {

    document.getElementById("btn2").setAttribute("href", "https://www.google.com/search?q=effect+of+pregnancy+on+diabetes&rlz=1C1CHBD_enIN927IN927&oq=effect+of+pregnancy+on+diabetes&aqs=chrome.0.69i59j0i512j0i22i30l5j0i15i22i30j0i22i30l2.4536j0j7&sourceid=chrome&ie=UTF-8");
    document.getElementById("headIntro").innerHTML = "Pregnancy";
    document.getElementById("small").innerHTML="Effects of Pregnancy on Diabetes";
    document.getElementById("p1").innerHTML="Pregnant women who can’t make enough insulin during late pregnancy develop gestational diabetes.Being overweight or obese is linked to gestational diabetes.";
    document.getElementById("p2").innerHTML=" Women who are overweight or obese may already have insulin resistance when they become pregnant.";
    document.getElementById("p3").innerHTML="Gaining too much weight during pregnancy may also be a factor.";

}
function glucose() {
    document.getElementById("btn2").setAttribute("href","https://www.google.com/search?q=how+glucose+affect+diabetes&rlz=1C1CHBD_enIN927IN927&oq=how+glucose+affect+diabetes&aqs=chrome..69i57.9496j0j7&sourceid=chrome&ie=UTF-8")
    document.getElementById("headIntro").innerHTML = "Glucose";
    document.getElementById("small").innerHTML="Effects of Glucose level on Diabetes";
    document.getElementById("p1").innerHTML="Hyperglycemia (high blood glucose) means there is too much sugar in the blood because the body lacks enough insulin. Associated with diabetes, hyperglycemia can cause vomiting, excessive hunger and thirst, rapid heartbeat, vision problems and other symptoms. Untreated hyperglycemia can lead to serious health problems."
    document.getElementById("p2").innerHTML="A person has impaired glucose tolerance, or pre-diabetes, with a fasting blood glucose of 100 mg/dL to 125 mg/dL.A person has hyperglycemia if their blood glucose is greater than 180 mg/dL one to two hours after eating."
    document.getElementById("p3").innerHTML="If you have hyperglycemia and it’s untreated for long periods of time, you can damage your nerves, blood vessels, tissues and organs."
}
function diastolic() {
    document.getElementById("btn2").setAttribute("href","https://www.google.com/search?q=how+diastolic+blood+pressure+affects+diabetes&rlz=1C1CHBD_enIN927IN927&oq=how+diastolic+blood+pressure+affects+diabetes&aqs=chrome..69i57.11528j0j7&sourceid=chrome&ie=UTF-8")
    document.getElementById("headIntro").innerHTML = "Diastolic Blood Pressure";
    document.getElementById("small").innerHTML="Effects of Diastolic blood pressure on Diabetes";
    document.getElementById("p1").innerHTML=" The diastolic pressure, refers to the pressure inside the artery when the heart is at rest and is filling with blood. "
    document.getElementById("p2").innerHTML=" High blood pressure is twice as likely to strike a person with diabetes than a person without diabetes. Left untreated, high blood pressure can lead to heart disease and stroke. "
    document.getElementById("p3").innerHTML=" In fact, a person with diabetes and high blood pressure is four times as likely to develop heart disease than someone who does not have either of the conditions. "
}
function triceps() {
    document.getElementById("btn2").setAttribute("href","https://www.google.com/search?q=how+triceps+or+skin+thickness+affect+diabetes&rlz=1C1CHBD_enIN927IN927&oq=how+triceps+or+skin+thickness+affect+diabetes&aqs=chrome..69i57.12666j0j7&sourceid=chrome&ie=UTF-8")
    document.getElementById("headIntro").innerHTML = "Triceps";
    document.getElementById("small").innerHTML="Effects of Skin Thickness on Diabetes";
    document.getElementById("p1").innerHTML="Skin thickening is frequently observed in patients with diabetes. Affected areas of skin can appear thickened, waxy, or edematous. These patients are often asymptomatic but can have a reduction in sensation and pain."
    document.getElementById("p2").innerHTML=" Although different parts of the body can be involved, the hands and feet are most frequently involved. Ultrasound evaluation of the skin can be diagnostic and exhibit thickened skin."
    document.getElementById("p3").innerHTML=" Subclinical generalized skin thickening is the most common type of skin thickening. "
}
function insulin() {
    document.getElementById("btn2").setAttribute("href","https://www.google.com/search?q=how+insulin+affects+diabetes&rlz=1C1CHBD_enIN927IN927&oq=how+insulin+affects+diabetes&aqs=chrome..69i57.15647j0j7&sourceid=chrome&ie=UTF-8")
    document.getElementById("headIntro").innerHTML = "Insulin";
    document.getElementById("small").innerHTML="Effects of Insulin on Diabetes";
    document.getElementById("p1").innerHTML="Insulin is a hormone that comes from a gland situated behind and below the stomach (pancreas)."
    document.getElementById("p2").innerHTML="Insulin is responsible for allowing glucose into your body's cells. When the glucose enters your cells, the amount of glucose in your bloodstream falls."
    document.getElementById("p3").innerHTML="When you have type 2 diabetes, your fat, liver, and muscle cells do not respond correctly to insulin. This is called insulin resistance."
}
function bmi() {
    document.getElementById("btn2").setAttribute("href","https://www.google.com/search?q=how+bmi+affects+diabetes&rlz=1C1CHBD_enIN927IN927&oq=how+bmi+affects+diabetes&aqs=chrome..69i57.7911j0j7&sourceid=chrome&ie=UTF-8")
    document.getElementById("headIntro").innerHTML = "Body Mass Index";
    document.getElementById("small").innerHTML="Effects of Bmi on Diabetes";
    document.getElementById("p1").innerHTML="The body mass index (BMI) is a measure that uses your height and weight to work out if your weight is healthy.";
    document.getElementById("p2").innerHTML="There is a close association between obesity and type 2 diabetes. The likelihood and severity of type 2 diabetes are closely linked with body mass index (BMI).";
    document.getElementById("p3").innerHTML="There is a seven times greater risk of diabetes in obese people compared to those of healthy weight, with a threefold increase in risk for overweight people.";
}
function dpf() {
    document.getElementById("btn2").setAttribute("href","https://www.google.com/search?q=how+diabetes+pedigree+function+or+genes+affect+diabetes&rlz=1C1CHBD_enIN927IN927&oq=how+diabetes+pedigree+function+or+genes+affect+diabetes&aqs=chrome..69i57.18530j0j9&sourceid=chrome&ie=UTF-8")
    document.getElementById("headIntro").innerHTML = "Diabetes Pedigree Function";
    document.getElementById("small").innerHTML="Effects of DPF on Diabetes";
    document.getElementById("p1").innerHTML="Diabetes Pedigree Function indicates the function which scores likelihood of diabetes based on family history. "
    document.getElementById("p2").innerHTML="The risk of developing type 2 diabetes increases with the number of affected family members. The increased risk is likely due in part to shared genetic factors, but it is also related to lifestyle influences (such as eating and exercise habits) that are shared by members of a family"
    document.getElementById("p3").innerHTML="If you have a family health history of diabetes, you are more likely to have prediabetes and develop diabetes. You are also more likely to get type 2 diabetes if you have had gestational diabetes, are overweight or obese, or are African American, American Indian, Asian American, Pacific Islander, or Hispanic."
}
function age() {
    document.getElementById("btn2").setAttribute("href","https://www.google.com/search?q=how+age+affects+diabetes&rlz=1C1CHBD_enIN927IN927&oq=how+age+affects+diabetes&aqs=chrome..69i57.19202j0j9&sourceid=chrome&ie=UTF-8")
    document.getElementById("headIntro").innerHTML = "Age";
    document.getElementById("small").innerHTML="Effects of Age on Diabetes";
    document.getElementById("p1").innerHTML="Age is a big risk factor for type 2. The older you are, the more likely you are to have it. That also holds true for preteens and teenagers, whose diabetes rates have climbed sharply in recent years."
    document.getElementById("p2").innerHTML="Type 2 diabetes most often develops in people over age 45, but more and more children, teens, and young adults are also developing it."
    document.getElementById("p3").innerHTML="The prevalence of both type 2 diabetes and prediabetes increases with advancing age."
}