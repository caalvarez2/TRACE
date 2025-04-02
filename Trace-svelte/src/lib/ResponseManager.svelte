<script lang="ts">
    import { responseStore } from '$lib/stores/responseStore';
  
    let parsedResponse: any = null;
  
    // Subscribe to the store and parse incoming data
    $: responseStore.subscribe((data) => {
      // Only parse if there is data
      parsedResponse = data ? parseResponse(data) : null;
    });
  
    function parseResponse(response: string | object) {
      if (typeof response === 'string') {
        try {
          return JSON.parse(response);
        } catch (error) {
          console.error("Failed to parse response string", error);
          return null;
        }
      } else if (typeof response === 'object') {
        return response;
      }
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
          <pre>{JSON.stringify(parsedResponse.body, null, 2)}</pre>
        </div>
      </div>
    {:else}
      <p>No valid response to display.</p>
    {/if}
  </div>
  