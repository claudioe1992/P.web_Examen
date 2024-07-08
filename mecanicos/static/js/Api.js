function getConductores(done) {

    const results = fetch("https://api.openf1.org/v1/drivers");

    results
        .then(response => response.json())
        .then(data => {
            done(data)
        });

};
getConductores(data => {
    const conductoresLista = document.getElementById('conductores-lista');
    // Obtener solo los primeros 6 conductores
    const primerosSeisConductores = data.slice(0, 6);
    primerosSeisConductores.forEach(conductor => {
        const article = document.createElement('article');
        article.innerHTML = `
        <div class="image-container">
            <img src="${conductor.headshot_url}" alt="${conductor.first_name} ${conductor.last_name}">
        </div>
        <h2>${conductor.first_name} ${conductor.last_name}</h2>
        <p>Equipo: ${conductor.team_name}</p>
        <p>País: ${conductor.country_code}</p>
    `;
        conductoresLista.appendChild(article);
    });
});

getConductores(data => {
    console.log(data);
    data.results.forEach(Conductores => {

        const article = document.createRange().createContextualFragment(/*html*/`
            <article>

                <div class="image-container">
                    <img src="${Conductores.headshot_url}" alt="Conductores"></img>
                </div>

                <h2>${Conductores.first_name}</h2>
                <h2>${Conductores.last_name}</h2>


            </article>
        `);

        const main = document.querySelector("main");

        main.append(article);

    });

});

/** 
https://api.openf1.org/v1/drivers
https://openf1.org/#drivers
https://www.youtube.com/watch?v=rfOrTHC6utU

*/