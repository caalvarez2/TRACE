<script lang="ts">
    import { responseStore } from '$lib/stores/responseStore';
    import ResponseManager from '$lib/ResponseManager.svelte';
    
    // Local state for the request inputs
    let url: string = "";
    let method: string = "GET";
    let headers: string = '{"Content-Type": "application/json"}';
    let payload: string = "";
    
    async function sendRequest() {
      console.log("=== Sending HTTP Request ===");
      console.log("URL:", url);
      console.log("Method:", method);
      console.log("Raw Headers:", headers);
      console.log("Raw Payload:", payload);
    
      // Convert headers and payload from string to object (if possible)
      let headersObj = {};
      try {
        headersObj = JSON.parse(headers);
        console.log("Parsed Headers:", headersObj);
      } catch (error) {
        console.error("Invalid JSON for headers", error);
        alert("Invalid JSON for headers");
        return;
      }
    
      let payloadObj = null;
      if (payload) {
        try {
          payloadObj = JSON.parse(payload);
          console.log("Parsed Payload:", payloadObj);
        } catch (error) {
          console.error("Invalid JSON for payload", error);
          alert("Invalid JSON for payload");
          return;
        }
      }
    
      const requestData = {
        url,
        method,
        headers: headersObj,
        payload: payloadObj
      };
      console.log("Final requestData to send:", requestData);
    
      try {
        console.log("Sending HTTP request to http://localhost:8000/tools/send");
        const res = await fetch("http://localhost:8000/tools/send", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(requestData)
        });
    
        console.log("HTTP response status:", res.status);
    
        if (!res.ok) {
          const errorData = await res.json();
          console.error("Error response from backend:", errorData);
          alert("Error: " + errorData.detail);
          return;
        }
    
        const data = await res.json();
        console.log("Received data from backend:", data);
        // Update the response store so that the Response Manager displays it
        responseStore.set(data);
      } catch (error) {
        console.error("Request failed", error);
        alert("Request failed: " + error);
      }
    }
  </script>
    
  <style>
    .form-container {
      margin: 1rem;
      padding: 1rem;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    .form-group {
      margin-bottom: 1rem;
    }
    label {
      display: block;
      margin-bottom: 0.5rem;
    }
    input,
    textarea,
    select {
      width: 100%;
      padding: 0.5rem;
      font-size: 1rem;
    }
    button {
      padding: 0.5rem 1rem;
      font-size: 1rem;
      cursor: pointer;
    }
  </style>
    
  <div class="form-container">
    <h2>Send HTTP Request</h2>
    <div class="form-group">
      <label for="url">URL</label>
      <input
        id="url"
        type="text"
        bind:value={url}
        placeholder="https://example.com/api"
      />
    </div>
    <div class="form-group">
      <label for="method">Method</label>
      <select id="method" bind:value={method}>
        <option value="GET">GET</option>
        <option value="POST">POST</option>
        <option value="PUT">PUT</option>
        <option value="PATCH">PATCH</option>
        <option value="DELETE">DELETE</option>
      </select>
    </div>
    <div class="form-group">
      <label for="headers">Headers (JSON)</label>
      <textarea
        id="headers"
        rows="4"
        bind:value={headers}
        placeholder={'{"Content-Type": "application/json"}'}
      ></textarea>
    </div>
    <div class="form-group">
      <label for="payload">Payload (JSON)</label>
      <textarea
        id="payload"
        rows="4"
        bind:value={payload}
        placeholder={'{"key": "value"}'}
      ></textarea>
    </div>
    <button on:click={sendRequest}>Send Request</button>
  </div>
    
  <!-- Include the Response Manager component to display the response -->
  <ResponseManager />
  