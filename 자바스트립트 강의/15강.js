const addItems = document.querySelector('.add-items');
const itemsList = document.querySelector('.plates');
const items = JSON.parse(localStorage.getItem("items")) || [];

function addItemList(e){
    e.preventDefault();
    const text = (this.querySelector("[name=item]")).value;
    const item = {
        text: text,
        done: false
    } 
    items.push(item);
    inputList(items, itemsList);
    //localstroage는  string만 인식, 그 전에 직렬화
    console.log(items);
    localStorage.setItem('items', JSON.stringify(items));
    this.reset();
}


function inputList(items = [], itemsList) {
    itemsList.innerHTML = items.map((item, i) => {
        return `
        <li>
            <input type="checkbox" data-index= ${i} id= "item${i}" ${item.done ? 'checked' : ''} />
            <label for="" data-index= ${i}>${item.text}</label>
        </li>
        `;
    }).join("");
}

function toggleDone(e){
    if (!e.target.matches('label')) return; // input tag가 html에서 못읽음 이유 모르겠음
    const el = e.target;
    const index = el.dataset.index;
    console.log(index);
    items[index].done = !items[index].done;
    localStorage.setItem('items', JSON.stringify(items));
    inputList(items, itemsList);
}

itemsList.addEventListener('click', toggleDone);
addItems.addEventListener("submit", addItemList);

inputList(items, itemsList);