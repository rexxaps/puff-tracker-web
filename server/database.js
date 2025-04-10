const fs = require('fs');
const path = require('path');

const dataDir = path.join(__dirname, 'data');
if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir);

function getTodayDate() {
    return new Date().toISOString().split('T')[0];
}

function getWeekNumber(d = new Date()) {
    d = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()));
    const yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1));
    const weekNo = Math.ceil((((d - yearStart) / 86400000) + 1) / 7);
    return `${d.getUTCFullYear()}-W${weekNo}`;
}

function getMonthKey(d = new Date()) {
    return `${d.getFullYear()}-${(d.getMonth() + 1).toString().padStart(2, '0')}`;
}

function getUserFilePath(userId) {
    const userDir = path.join(dataDir, userId);
    if (!fs.existsSync(userDir)) fs.mkdirSync(userDir);
    return path.join(userDir, 'data.json');
}

function loadUserData(userId) {
    const filePath = getUserFilePath(userId);
    if (!fs.existsSync(filePath)) {
        return {
            dailyCount: 0,
            weeklyCount: 0,
            monthlyCount: 0,
            totalMonths: [],
            lastDay: getTodayDate(),
            lastWeek: getWeekNumber(),
            lastMonth: getMonthKey()
        };
    }
    const raw = fs.readFileSync(filePath);
    return JSON.parse(raw);
}

function saveUserData(userId, data) {
    const filePath = getUserFilePath(userId);
    fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
}

function updateCounts(userId) {
    const data = loadUserData(userId);
    const today = getTodayDate();
    const thisWeek = getWeekNumber();
    const thisMonth = getMonthKey();

    if (data.lastDay !== today) {
        data.dailyCount = 0;
        data.lastDay = today;
    }

    if (data.lastWeek !== thisWeek) {
        data.weeklyCount = 0;
        data.lastWeek = thisWeek;
    }

    if (data.lastMonth !== thisMonth) {
        // Перед сбросом monthlyCount сохраняем в totalMonths
        data.totalMonths.push({
            month: data.lastMonth,
            count: data.monthlyCount
        });
        data.monthlyCount = 0;
        data.lastMonth = thisMonth;
    }

    saveUserData(userId, data);
    return data;
}

function incrementUser(userId) {
    const data = updateCounts(userId);
    data.dailyCount += 1;
    data.weeklyCount += 1;
    data.monthlyCount += 1;
    saveUserData(userId, data);
    return data;
}

module.exports = {
    loadUserData,
    updateCounts,
    incrementUser
};
