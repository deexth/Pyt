"use strict"


function slider_change() {
    var slider = document.getElementById("slider").value;
    document.getElementById("rate").innerHTML = slider + "%";
    document.getElementById("rate_new").innerHTML = slider + "%";
    return slider
}

function new_value() {
    return slider_change()
}

function compute() {
    let p = document.getElementById("principal").value;
    let h = document.getElementsByClassName("hidden");
    let am = document.getElementById("amount");
    // let rate = document.getElementById("rate_new").value;
    let res = document.getElementById("result");
    let t_years = document.getElementById("total_years");
    let currentYear = new Date().getFullYear();
    let years = document.getElementById("years").value;

    if (p < 1) {
        alert("Enter a positive number");
    }

    Array.from(h).forEach((x) => {
        if (x.style.display === "none") {
            x.style.display = "block";
        } else {
            x.style.display = "block";
        }
    })

    

    am.innerHTML = p;
    res.innerHTML = (Number(p) * Number(new_value()) * Number(years)) / 100
    t_years.innerHTML = Number(years) + currentYear;
}

