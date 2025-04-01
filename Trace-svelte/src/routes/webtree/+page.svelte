<script>
    import { onMount } from 'svelte';
    import TreeGraph from '$lib/TreeGraph.svelte'; // Path to your D3 tree component or recursive component
  
    let treeData = [];
    let loading = true;
    let error = null;
  
    onMount(async () => {
      console.log("Starting to fetch tree data...");
      try {
        const res = await fetch('http://localhost:8000/webtree/');
        console.log("Fetch response:", res);
        if (!res.ok) {
          throw new Error(`HTTP error: ${res.status}`);
        }
        treeData = await res.json();
        console.log("Fetched tree data:", treeData);
      } catch (err) {
        error = err.message;
        console.error("Error fetching tree data:", err);
      } finally {
        loading = false;
        console.log("Loading complete. treeData:", treeData);
      }
    });
  </script>
  
  {#if loading}
    <p>Loading tree data...</p>
  {:else if error}
    <p style="color:red">Error: {error}</p>
  {:else}
    <TreeGraph data={treeData} />
  {/if}
  