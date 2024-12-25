var audio = new Audio('assets/sentmessage.mp3');
var contactString = "<div class='social'> <a target='_blank' href='tel:+2347066253101'> <div class='socialItem' id='call'><img class='socialItemI' src='images/phone.svg'/><label class='number'></label></label></div> </a> <a href='mailto:varshithvh@gmail.com'> <div class='socialItem'><img class='socialItemI' src='images/gmail.svg' alt=''></div> </a> <a target='_blank' href='https://github.com/adetayo-Adebayo284'> <div class='socialItem'><img class='socialItemI' src='images/github.svg' alt=''></div> </a> <a target='_blank' href='https://wa.me/7066253101'> <div class='socialItem'><img class='socialItemI' src='images/whatsapp.svg' alt=''>";
var addressString = "<div class='mapview'><iframe src='https://www.google.com/maps/dir//Moodbidri+private+Bus+Stand,+Bus+Stand+Rd,+Mudbidri,+Karnataka+574227/@13.0639,74.9991985,15z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3ba4ab3d49331379:0x17be05cb5b69caa2!2m2!1d74.9957298!2d13.0680955?hl=en' class='map'></iframe></div><label class='add'><address>Gateway ICT Polytechnic Saapade, <br> Ogun State. Nigeria.</address>";

function startFunction() {
    setLastSeen();
    waitAndResponce("intro");
}

function setLastSeen() {
    var date = new Date();
    var lastSeen = document.getElementById("lastseen");
    lastSeen.innerText = "last seen today at " + date.getHours() + ":" + date.getMinutes()
}


function closeFullDP() {
    var x = document.getElementById("fullScreenDP");
    if (x.style.display === 'flex') {
        x.style.display = 'none';
    } else {
        x.style.display = 'flex';
    }
}

function openFullScreenDP() {
    var x = document.getElementById("fullScreenDP");
    if (x.style.display === 'flex') {
        x.style.display = 'none';
    } else {
        x.style.display = 'flex';
    }
}


function isEnter(event) {
    if (event.keyCode == 13) {
        sendMsg();
    }
}

function sendMsg() {
    var input = document.getElementById("inputMSG");
    var ti = input.value;
    if (input.value == "") {
        return;
    }
    var date = new Date();
    var myLI = document.createElement("li");
    var myDiv = document.createElement("div");
    var greendiv = document.createElement("div");
    var dateLabel = document.createElement("label");
    dateLabel.innerText = date.getHours() + ":" + date.getMinutes();
    myDiv.setAttribute("class", "sent");
    greendiv.setAttribute("class", "green");
    dateLabel.setAttribute("class", "dateLabel");
    greendiv.innerText = input.value;
    myDiv.appendChild(greendiv);
    myLI.appendChild(myDiv);
    greendiv.appendChild(dateLabel);
    document.getElementById("listUL").appendChild(myLI);
    var s = document.getElementById("chatting");
    s.scrollTop = s.scrollHeight;
    setTimeout(function () { waitAndResponce(ti) }, 1500);
    input.value = "";
    playSound();
}

function waitAndResponce(inputText) {
    var lastSeen = document.getElementById("lastseen");
    lastSeen.innerText = "typing...";
    var name = "";

    if (inputText.toLowerCase().includes("my name is")) {
        name = inputText.substring(inputText.indexOf("is") + 2).trim();
        if (name.toLowerCase().includes("adebayo") || name.toLowerCase().includes("adetayo")) {
            sendTextMessage("Ohh! That's my name too");
        }
        inputText = "input";
    } else if ((inputText.toLowerCase().includes("clear the chats")) || (inputText.toLowerCase().includes("clear the chats")) || (inputText.toLowerCase().includes("clear our chat")) || (inputText.toLowerCase().includes("clear our chats")) || (inputText.toLowerCase().includes("erase our chats"))) {
        clearChat();
    } else if (inputText.toLowerCase().trim() === "time") {
        var date = new Date();
        sendTextMessage("Current time is " + date.getHours() + ":" + date.getMinutes());
    } else if(inputText.toLowerCase().includes("clear the chats") || inputText.toLowerCase().includes("clear the chat")){
        clearChat();
    } else if(inputText.toLowerCase().trim() === "date"){
        var date = new Date();
        sendTextMessage("Current date is " + date.getDate() + "/" + date.getMonth() + "/" + date.getFullYear());
    } else {
        // Process the inputText against patterns from the JSON file
        fetch('./process/response.php')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            let responseFound = false;

            for (const category in data) {
                if (data.hasOwnProperty(category)) {
                    data[category].forEach(item => {
                        const regex = new RegExp(item.pattern, "i");
                        if (regex.test(inputText)) {
                            sendTextMessage(item.response);
                            responseFound = true;
                        }
                    });
                }
            }

            if (!responseFound) {
                sendTextMessage("I'm not sure how to respond to that. Can you please ask something else?");
            }

            lastSeen.innerText = "last seen today at " + new Date().toLocaleTimeString();
        })
        .catch(error => {
            console.error('Error fetching JSON:', error);
            sendTextMessage("There was an error processing your request. Please try again later.");
            lastSeen.innerText = "last seen today at " + new Date().toLocaleTimeString();
        });
    
    }
}

function clearChat() {
    document.getElementById("listUL").innerHTML = "";
    setLastSeen();
}

function sendTextMessage(textToSend) {
    setTimeout(setLastSeen, 1000);
    var date = new Date();
    var myLI = document.createElement("li");
    var myDiv = document.createElement("div");
    var greendiv = document.createElement("div");
    var dateLabel = document.createElement("label");
    dateLabel.setAttribute("id", "sentlabel");
    dateLabel.id = "sentlabel";
    dateLabel.innerText = date.getHours() + ":" + date.getMinutes();
    myDiv.setAttribute("class", "received");
    greendiv.setAttribute("class", "grey");
    greendiv.innerHTML = textToSend;
    myDiv.appendChild(greendiv);
    myLI.appendChild(myDiv);
    greendiv.appendChild(dateLabel);
    document.getElementById("listUL").appendChild(myLI);
    var s = document.getElementById("chatting");
    s.scrollTop = s.scrollHeight;
    playSound();
}


function sendResponse() {
    setTimeout(setLastSeen, 1000);
    var date = new Date();
    var myLI = document.createElement("li");
    var myDiv = document.createElement("div");
    var greendiv = document.createElement("div");
    var dateLabel = document.createElement("label");
    dateLabel.innerText = date.getHours() + ":" + date.getMinutes();
    myDiv.setAttribute("class", "received");
    greendiv.setAttribute("class", "grey");
    dateLabel.setAttribute("class", "dateLabel");
    greendiv.innerText = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. ";
    myDiv.appendChild(greendiv);
    myLI.appendChild(myDiv);
    greendiv.appendChild(dateLabel);
    document.getElementById("listUL").appendChild(myLI);
    var s = document.getElementById("chatting");
    s.scrollTop = s.scrollHeight;
    playSound();
}

function playSound() {
    audio.play();
}


















