

const localURL = 'http://localhost:5000';

const post = (endpoint, data)=> {
    console.log(data)
    console.log("Posting1")
    fetch(`${localURL}${endpoint}`,
    {method: 'POST',
    headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},
    body: JSON.stringify(data)})
console.log("Posting")

};
//one item is 1 dictionary with 4 fields: {name: A, category: B, amount: C, storeId: D}
export const postItem = (name, category, amount, storeId) =>{
    return post("/newItem", { name, category, amount, storeId})
   
};