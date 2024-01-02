//패치하기
function loaditems() {
  return fetch("data/data.json")
    .then((Response) => Response.json())
    .then((json) => json.items);
}

//HTML라인을 리스트로 바꾸기
function displayItems(items) {
  const container = document.querySelector(".items");
  container.innerHTML = items.map((item) => createHTMLString(item)).join("");
}

//HTML 라인
function createHTMLString(item) {
  return `
        <li class="item">
        <img src="${item.image}" alt="${item.type}" class="item_thumbnail" />
        <span class="item_description">${item.gender}, ${item.size}</span>
      </li>
      `;
}

//메인
loaditems()
  .then((items) => {
    displayItems(items);
    //seteventListeners(items);
  })
  .catch(console.log);
