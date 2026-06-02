export async function fetchItems() {
  const res = await fetch("http://localhost:8000/api/items");
  return res.json();
}
