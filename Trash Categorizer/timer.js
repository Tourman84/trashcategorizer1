
//Define vars to hold time values
let seconds = 0;
let minutes = 0;
let hours = 0;

//Define vars to hold "display" value
let displaySeconds = 0;
let displayMinutes = 0;
let displayHours = 0;

//Define var to hold setInterval() function
let interval = null;

//Is the stopwatch stopped or started
let status = "stopped";

//Stopwatch function 
function stopWatch(){

    seconds++;

    //Switches from seconds to minutes to hours when over 60 of each value
    if(seconds / 60 === 1){
        seconds = 0;
        minutes++;

        if(minutes / 60 === 1){
            minutes = 0;
            hours++;
        }

    }

    //Makes sure numbers are 2 digits due to being time
    if(seconds < 10){
        displaySeconds = "0" + seconds.toString();
    }
    else{
        displaySeconds = seconds;
    }

    if(minutes < 10){
        displayMinutes = "0" + minutes.toString();
    }
    else{
        displayMinutes = minutes;
    }

    if(hours < 10){
        displayHours = "0" + hours.toString();
    }
    else{
        displayHours = hours;
    }

    //Resets the information in the HTML to display time
    document.getElementById("display").innerHTML = "<br><br>" + displayHours + ":" + displayMinutes + ":" + displaySeconds;

}



function startStop(){

    if(status === "stopped"){

        //Starts the stopwatch and lets the program know it is running
        interval = window.setInterval(stopWatch, 1000);
        document.getElementById("startStop").innerHTML = "<span class='material-icons'>&#xe034;</span>";
        status = "started";

    }
    else{
        //Tells the program that the stopwatch has stopped
        window.clearInterval(interval);
        document.getElementById("startStop").innerHTML = "<span class='material-icons'>&#xe039;</span>";
        status = "stopped";

    }

}

//Function to reset the stopwatch
function reset(){

    window.clearInterval(interval);
    seconds = 0;
    minutes = 0;
    hours = 0;
    document.getElementById("display").innerHTML = "<br><br>00:00:00";
    document.getElementById("startStop").innerHTML = "<span class='material-icons'>&#xe039;</span>";

}