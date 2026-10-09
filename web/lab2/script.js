console.log('script.js подключён');

const films = [
    { name: 'Семь',           year: 1995, rating: 8.6 },
    { name: 'Начало',         year: 2010, rating: 8.8 },
    { name: 'Крёстный отец',  year: 1972, rating: 9.2 },
    { name: 'Престиж',        year: 2006, rating: 8.5 }
];

let totalRating = 0;

films.forEach(function (film) {
    totalRating = totalRating + film.rating;
});

console.log('Сумма рейтингов:', totalRating);

const bill = {
    bill: films,
    result: totalRating
};

console.log(JSON.stringify(bill));

const now = new Date();
console.log('Дата и время:', now);
console.log('Формат:', now.toLocaleString('ru-RU'));


const copyBtn   = document.getElementById('copy-btn');
const styleBtn  = document.getElementById('style-btn');
const searchInput = document.getElementById('search');
const filmsList = document.getElementById('films-list');
const output    = document.getElementById('output');

copyBtn.addEventListener('click', function () {
    const items = filmsList.querySelectorAll('li');
    let text = '';

    items.forEach(function (item) {
        text = text + item.textContent + '; ';
    });

    output.textContent = output.textContent + ' ' + text;
});

styleBtn.addEventListener('click', function () {
    const items = filmsList.querySelectorAll('li');

    items.forEach(function (item) {
        item.classList.toggle('highlight');
    });
});

searchInput.addEventListener('input', function () {
    const query = searchInput.value.toLowerCase().trim();
    const items = filmsList.querySelectorAll('li');

    items.forEach(function (item) {
        const originalText = item.dataset.original || item.textContent;
        item.dataset.original = originalText;

        if (query === '') {
            item.innerHTML = originalText;
            item.classList.remove('found');
            return;
        }

        const index = originalText.toLowerCase().indexOf(query);

        if (index !== -1) {
            const before = originalText.slice(0, index);
            const match  = originalText.slice(index, index + query.length);
            const after  = originalText.slice(index + query.length);

            item.innerHTML = before + '<span class="mark">' + match + '</span>' + after;
            item.classList.add('found');
        } else {
            item.innerHTML = originalText;
            item.classList.remove('found');
        }
    });
});