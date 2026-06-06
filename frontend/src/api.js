const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

async function request(path, options) {
  const response = await fetch(`${API_URL}${path}`, options);

  if (!response.ok) {
    const body = await response.json().catch(() => ({}));
    throw new Error(body.detail || `Request failed with status ${response.status}`);
  }

  return response.status === 204 ? null : response.json();
}

export async function fetchItems() {
  return request("/api/items");
}

export async function createItem(item) {
  return request("/api/items", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(item),
  });
}

export async function updateItem(itemId, item) {
  return request(`/api/items/${itemId}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(item),
  });
}

export async function deleteItem(itemId) {
  return request(`/api/items/${itemId}`, { method: "DELETE" });
}
