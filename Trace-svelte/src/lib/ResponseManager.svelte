<script lang="ts">
  import { responseStore } from '$lib/stores/responseStore';
  
  let parsedResponse: any = null;
  
  // Helper function to determine if a string is valid JSON
  function isJson(str: string): boolean {
    try {
      JSON.parse(str);
      return true;
    } catch (e) {
      return false;
    }
  }
  
  // Subscribe to the store and parse incoming data
  $: responseStore.subscribe((data) => {
    console.log("Response Manager received data:", data);
    parsedResponse = data ? parseResponse(data) : null;
    console.log("Parsed response:", parsedResponse);
  });
  
  function parseResponse(response: string | object) {
    console.log("Parsing response:", response);
    if (typeof response === 'string') {
      try {
        const parsed = JSON.parse(response);
        console.log("Successfully parsed string response:", parsed);
        return parsed;
      } catch (error) {
        console.error("Failed to parse response string", error);
        return response;
      }
    } else if (typeof response === 'object') {
      console.log("Response is an object:", response);
      return response;
    }
    console.warn("Response is neither string nor object:", response);
    return null;
  }
</script>
  
<style>
  .response-container {
    padding: 1rem;
    background-color: #f5f5f5;
    border-radius: 5px;
    margin: 1rem 0;
    font-family: sans-serif;
  }
  .response-header {
    font-weight: bold;
    margin-bottom: 0.5rem;
  }
  .response-body {
    white-space: pre-wrap;
    font-family: monospace;
  }
</style>
  
<div class="response-container">
  <div class="response-header">HTTP Response</div>
  {#if parsedResponse}
    <div>
      <div><strong>Status:</strong> {parsedResponse.status}</div>
      <div><strong>Headers:</strong></div>
      <ul>
        {#each Object.entries(parsedResponse.headers) as [key, value]}
          <li>{key}: {value}</li>
        {/each}
      </ul>
      <div class="response-body">
        <strong>Body:</strong>
        {#if typeof parsedResponse.body === 'string' && isJson(parsedResponse.body)}
          <pre>{JSON.stringify(JSON.parse(parsedResponse.body), null, 2)}</pre>
        {:else}
          <pre>{parsedResponse.body}</pre>
        {/if}
      </div>
    </div>
  {:else}
    <p>No valid response to display.</p>
  {/if}
</div>
