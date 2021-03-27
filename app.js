// 0 == Number
// 1 == Lower
// 2 == Higher

let max = 100;
let min = 1;
let status;
button_pressed = true;
let attempts = 1
let randInt;
let IsNumber = false;

function process(bleh){
    status = bleh;

    if (status == 0){
        IsNumber = true;
    }else if(status == 1){
        max = randInt;
    }else if(status == 2){
        min = randInt;
    }

    attempts = attempts + 1;
    randInt = Math.floor((Math.random() * ((max - min) + 1)) + min);
    $("#realQuestion").html(`Is your number ${randInt}?`);    
    console.log(max)
    console.log(min)
    console.log("Attempts == " + attempts)
    if(IsNumber == true){
        attempts = attempts - 1
        $(".btn").attr("class", "invisible btn")
        $("#again").attr("class", "visible btn")
        $("#realQuestion").html(`WoW it took ${attempts} to guess your number.`)
    }
}

function game(){
    $("h2").attr("class", "invisible");
    $(".answer").attr("class", "visible btn");
    $("#ready").attr("class", "invisible")
    randInt = Math.floor((Math.random() * ((max - min) + 1)) + min);
    $("#realQuestion").html(`Is your number ${randInt}?`);
}

$(document).ready(
    $("#Higher, #Lower, #Number, #ready").hover(
        function(){
            $(this).css("background-color", "#949494")
            $(this).css("color", "#FFF")
        },
        function(){
            $(this).css("background-color", "#000")
            $(this).css("color", "#FFF")
        }
    )
)
