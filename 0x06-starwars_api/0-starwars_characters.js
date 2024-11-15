#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// URL du film correspondant à l'ID
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);

  if (!filmData.characters) {
    console.error('No characters found for this movie.');
    return;
  }

  // Itère à travers chaque URL de personnage et affiche le nom
  const printCharacterName = (characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  };

  // Utilise `forEach` pour chaque personnage de la liste
  filmData.characters.forEach(printCharacterName);
});
