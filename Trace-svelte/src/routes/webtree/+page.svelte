<script lang="ts">
  import { page } from '$app/stores';
  import { onMount, onDestroy } from 'svelte';
  import TreeGraph from '$lib/TreeGraph.svelte';

  interface TreeNodeData {
    name: string;
    children: TreeNodeData[];
    [key: string]: any; // For additional properties like severity
  }

  let treeData: { name: string; children: TreeNodeData[] } | null = null;
  let loading: boolean = true;
  let error: string | null = null;
  let newUrl: string = '';
  let refreshInterval: number | null = null;

  $: projectId = $page.url.searchParams.get('projectId');

  // Function to load tree data
  async function loadTreeData(): Promise<void> {
    try {
      loading = true;
      const res = await fetch(`http://localhost:8000/webtree/?projectId=${projectId || ''}`);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const result = await res.json();

      console.log("Tree data response:", result);

      if (Array.isArray(result)) {
        treeData = {
          name: 'ROOT',
          children: result
        };
      } else {
        treeData = null;
      }

      console.log("Final treeData:", treeData);
    } catch (err: unknown) {
      error = err instanceof Error ? err.message : String(err);
    } finally {
      loading = false;
    }
  }

  // Function to add a new URL
  async function addUrl(event: SubmitEvent): Promise<void> {
    event.preventDefault();
    if (!newUrl) return;

    try {
      loading = true;
      const res = await fetch(`http://localhost:8000/webtree/add-url?url=${encodeURIComponent(newUrl)}`, {
        method: 'POST',
      });
      
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const result = await res.json();
      
      console.log("URL added response:", result);
      // Reload tree data
      await loadTreeData();
      // Reset form
      newUrl = '';
    } catch (err: unknown) {
      error = err instanceof Error ? err.message : String(err);
    } finally {
      loading = false;
    }
  }

  onMount(async () => {
    await loadTreeData();
    // Set up auto-refresh every 15 seconds
    refreshInterval = window.setInterval(loadTreeData, 15000);
  });

  onDestroy(() => {
    // Clear the interval when component is destroyed
    if (refreshInterval !== null) {
      window.clearInterval(refreshInterval);
    }
  });
</script>

<style>
  .webtree-container {
    padding: 2rem;
    max-width: 100%;
    min-height: 100vh;
    background-color: #f9fafb;
    font-family: 'Segoe UI', sans-serif;
  }

  h1 {
    font-size: 2rem;
    margin-bottom: 1rem;
    color: #1f2937;
    text-align: center;
  }

  .status-message {
    text-align: center;
    color: #6b7280;
    font-size: 1.2rem;
  }

  .error {
    color: red;
  }

  .controls {
    margin: 1rem auto;
    max-width: 600px;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .url-form {
    display: flex;
    gap: 0.5rem;
  }

  input {
    flex: 1;
    padding: 0.5rem;
    border: 1px solid #d1d5db;
    border-radius: 0.375rem;
  }

  button {
    padding: 0.5rem 1rem;
    background-color: #3b82f6;
    color: white;
    border: none;
    border-radius: 0.375rem;
    cursor: pointer;
    transition: background-color 0.2s;
  }

  button:hover {
    background-color: #2563eb;
  }

  .refresh-button {
    align-self: center;
    margin-top: 0.5rem;
  }
</style>

<div class="webtree-container">
  <h1>WebTree</h1>

  <div class="controls">
    <form class="url-form" on:submit={addUrl}>
      <input 
        type="text" 
        bind:value={newUrl} 
        placeholder="Enter a URL to add to the tree" 
      />
      <button type="submit">Add URL</button>
    </form>
    <button class="refresh-button" on:click={loadTreeData}>Refresh Tree</button>
  </div>

  {#if loading}
    <p class="status-message">Loading tree data...</p>
  {:else if error}
    <p class="status-message error">Error: {error}</p>
  {:else if treeData && Array.isArray(treeData.children) && treeData.children.length > 0}
    <TreeGraph data={treeData} />
  {:else}
    <p class="status-message">No tree data to display.</p>
  {/if}
</div>
