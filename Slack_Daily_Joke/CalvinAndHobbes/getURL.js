#!/usr/bin/node

const { getImage } = require("gocomics-api")
const fs = require("fs")

var date = new Date()
var year = date.getFullYear()
var month = date.getMonth() + 1
var day = date.getDate() - 1

async function Data() {
    let res = await getImage({
	date: [year,month,day],
	comicName: "calvinandhobbes",
	URLOnly: true
    })
    res = day + "/" + month + "/" + year + "\n" + res
    if (res.includes("https://assets.amuniversal.com/")) {
	fs.writeFile("hobbes.txt", res, function(err) {
	    if (err) return console.log(err)
	});
    }
}
Data()
