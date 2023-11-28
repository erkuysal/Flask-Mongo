const timePeriods = [
    { period: "earlyMorning", messages: ["Good Morning?", "Shh, sun hasn't risen yet!", "A new day, actually."], color: "#ffebc6" },
    { period: "morning", messages: ["Good Morning!", "Have a great morning!", "Stay productive."], color: "#ffe6a8" },
    { period: "afternoon", messages: ["Good Afternoon!", "Time for a break!", "Keep up the good work."], color: "#ffe27f" },
    { period: "evening", messages: ["Good Evening!", "Enjoy your evening!", "Reflect on your day."], color: "#ffb768" },
    { period: "night", messages: ["Good Night!", "Sweet dreams!", "Rest well."], color: "#292929" }
];

function getCurrentTimePeriod() {
    const now = new Date();
    const currentHour = now.getHours();

    if (currentHour >= 3 && currentHour < 6) {
        return "earlyMorning";
    } else if (currentHour >= 6 && currentHour < 12) {
        return "morning";
    } else if (currentHour >= 12 && currentHour < 17) {
        return "afternoon";
    } else if (currentHour >= 17 && currentHour < 20) {
        return "evening";
    } else if (currentHour >= 20 || currentHour < 3) {
        return "night";
    }
}

function getRandomMessage(messages) {
    const randomIndex = Math.floor(Math.random() * messages.length);
    return messages[randomIndex];
}

function updateMessageAndBackground() {
    const currentTimePeriod = getCurrentTimePeriod();

    const timePeriodObject = timePeriods.find(period => period.period === currentTimePeriod);
    const randomMessage = getRandomMessage(timePeriodObject.messages);

    document.getElementById("message").textContent = randomMessage;
    document.body.style.backgroundColor = timePeriodObject.color;
}


updateMessageAndBackground();

setInterval(updateMessageAndBackground, 1000 * 60 * 60); // Update every hour (in milliseconds)
