function loaditems() {
  return fetch("data/data.json")
    .then((Response) => Response.json())
    .then((json) => json.items);
}

loaditems()
  .then((items) => {
    //displayItems(items);
    //seteventListeners(items);
  })
  .catch(console.log);
