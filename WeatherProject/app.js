const express = require("express")
const app = express();
const https = require('https');
const bodyParser = require("body-parser")
app.use(bodyParser.urlencoded({extended:true}))
app.get("/", function(req,res){
    res.sendFile(__dirname+ "/index.html")
})
app.post('/',function(req,res){
    console.log(req.body.cityName)
    const query = req.body.cityName
    const apiKey = '1d843489501448e9848162439231001'
    const url ='https://api.weatherapi.com/v1/current.json?key='+apiKey+'&q='+ query+'&aqi=yes'
    https.get(url, function(response){
        console.log(response)
        response.on("data", function(data){
           const weatherData =JSON.parse(data)
           
           const temp = weatherData.current.temp_c
           const icon = weatherData.current.condition.icon
           res.write(`<h1>The temprature in `+query+` is ${temp}</h1>`)
           res.write("<img src=" + icon+">")
        })
    })
})
// const query = 'Sofia'
//     const apiKey = '1d843489501448e9848162439231001'
//     const url ='https://api.weatherapi.com/v1/current.json?key='+apiKey+'&q='+ query+'&aqi=yes'
//     https.get(url, function(response){
//         console.log(response)
//         response.on("data", function(data){
//            const weatherData =JSON.parse(data)
           
//            const temp = weatherData.current.temp_c
//            const icon = weatherData.current.condition.icon
//            res.write(`<h1>The temprature in `+query+` is ${temp}</h1>`)
//            res.write("<img src=" + icon+">")
//         })
//     })
app.listen(3000,function(){
    console.log("server is ok")
})