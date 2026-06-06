import ItemList from "./components/ItemList";

export default function App() {
  return (
    <main className="app-shell">
      <header>
        <p className="eyebrow">Foundation workspace</p>
        <h1>Agentic SDLC Prototype</h1>
        <p className="subtitle">
          A working CRUD baseline for the governed generation engine.
        </p>
      </header>
      <ItemList />
    </main>
  );
}
