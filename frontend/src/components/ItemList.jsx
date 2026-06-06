import { useEffect, useState } from "react";
import { createItem, deleteItem, fetchItems, updateItem } from "../api";

export default function ItemList() {
  const [items, setItems] = useState([]);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [editingId, setEditingId] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    loadItems();
  }, []);

  async function loadItems() {
    try {
      setLoading(true);
      setError("");
      setItems(await fetchItems());
    } catch (requestError) {
      setError(requestError.message);
    } finally {
      setLoading(false);
    }
  }

  function resetForm() {
    setName("");
    setDescription("");
    setEditingId(null);
  }

  async function handleSubmit(event) {
    event.preventDefault();
    const payload = { name: name.trim(), description: description.trim() || null };

    if (!payload.name) {
      setError("Name is required.");
      return;
    }

    try {
      setError("");
      if (editingId === null) {
        await createItem(payload);
      } else {
        await updateItem(editingId, payload);
      }
      resetForm();
      await loadItems();
    } catch (requestError) {
      setError(requestError.message);
    }
  }

  function beginEdit(item) {
    setEditingId(item.id);
    setName(item.name);
    setDescription(item.description || "");
  }

  async function handleDelete(itemId) {
    try {
      setError("");
      await deleteItem(itemId);
      if (editingId === itemId) {
        resetForm();
      }
      await loadItems();
    } catch (requestError) {
      setError(requestError.message);
    }
  }

  return (
    <section className="workspace">
      <form className="item-form" onSubmit={handleSubmit}>
        <h2>{editingId === null ? "Create item" : "Edit item"}</h2>
        <label>
          Name
          <input
            value={name}
            onChange={(event) => setName(event.target.value)}
            placeholder="Enterprise backend template"
          />
        </label>
        <label>
          Description
          <textarea
            value={description}
            onChange={(event) => setDescription(event.target.value)}
            placeholder="Optional context"
            rows="4"
          />
        </label>
        <div className="form-actions">
          <button type="submit">
            {editingId === null ? "Add item" : "Save changes"}
          </button>
          {editingId !== null && (
            <button type="button" className="secondary" onClick={resetForm}>
              Cancel
            </button>
          )}
        </div>
      </form>

      <div className="item-panel">
        <div className="panel-heading">
          <h2>Items</h2>
          <span>{items.length}</span>
        </div>
        {error && <p className="error">{error}</p>}
        {loading ? (
          <p className="muted">Loading items...</p>
        ) : items.length === 0 ? (
          <p className="muted">No items yet. Create the first one.</p>
        ) : (
          <ul className="item-list">
            {items.map((item) => (
              <li key={item.id}>
                <div>
                  <strong>{item.name}</strong>
                  <p>{item.description || "No description"}</p>
                </div>
                <div className="item-actions">
                  <button
                    type="button"
                    className="secondary"
                    onClick={() => beginEdit(item)}
                  >
                    Edit
                  </button>
                  <button
                    type="button"
                    className="danger"
                    onClick={() => handleDelete(item.id)}
                  >
                    Delete
                  </button>
                </div>
              </li>
            ))}
          </ul>
        )}
      </div>
    </section>
  );
}
