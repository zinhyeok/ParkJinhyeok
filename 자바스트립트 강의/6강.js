const endpoint = 'https://gist.githubusercontent.com/Miserlou/c5cd8364bf9b2420bb29/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json';

const citiesList = [];

//fecth is a method that request info to server and return promise type 
fetch(endpoint)
  .then(blob => blob.json())
  .then(data => citiesList.push(...data));

function findMatches(wordToMatch, cities) {
  return cities.filter(place => {
    //RegExp is used when we search text with pattern 
    // g means global and i means do not concentrate on capital 
    const regex = new RegExp(wordToMatch, 'gi');
    return place.city.match(regex) || place.state.match(regex)
  });
}

//population에 comma추가 (href : stackoverflow)
function numberWithCommas(x) {
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

//비동기처리 위해  async 처리(의미 있으려나..?)
async function displayMatches() {
  const matchArray = findMatches(this.value, citiesList);
  const html = matchArray.map(place => {
    const regex = new RegExp(this.value, 'gi');
    const cityName = place.city.replace(regex, `<span class="hl">${this.value}</span>`);
    const stateName = place.state.replace(regex, `<span class="hl">${this.value}</span>`);
    return `
      <li>
        <span class="name">${cityName}, ${stateName}</span>
        <span class="population">${numberWithCommas(place.population)}</span>
      </li>
    `;
  }).join('');
  suggestions.innerHTML = html;
}

const searchInput = document.querySelector('.search');
const suggestions = document.querySelector('.suggestions');

searchInput.addEventListener('change', displayMatches);
searchInput.addEventListener('keyup', displayMatches);