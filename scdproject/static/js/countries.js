document.addEventListener('DOMContentLoaded',() => {
  
    const countries = document.querySelector('#countries');

    fetch('https://restcountries.com/v2/all').then(res => {
        return res.json();
    }).then(data => {
        let output = "";
        data.forEach(country => {
           output += `<option value="${country.name}">${country.name}</option>`;
        });
        countries.innerHTML = output;

    }).catch(err => {
        console.log(err);
    })

});