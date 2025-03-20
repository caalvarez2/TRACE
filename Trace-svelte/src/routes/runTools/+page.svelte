<script lang="ts">
    // Adjust the API base URL if necessary
    const API_BASE_URL = 'http://localhost:8000';
  
    async function runCrawler() {
      try {
        const res = await fetch(`${API_BASE_URL}/tools/run-crawler`, {
          method: 'POST'
        });
        if (!res.ok) {
          console.error('Error calling crawler endpoint:', res.status, res.statusText);
          alert('Failed to run crawler. Check console for details.');
          return;
        }
        const data = await res.json();
        console.log('Crawler response:', data);
        if (data.success) {
          alert('Crawler executed successfully. Check server console for the tree graph.');
        } else {
          alert('Crawler encountered an error: ' + data.error);
        }
      } catch (error) {
        console.error('Network or fetch error:', error);
        alert('Failed to run crawler. Check console for error details.');
      }
    }
  </script>
  
  <style>
    main {
      max-width: 600px;
      margin: 2rem auto;
      padding: 1rem;
      border-radius: 8px;
      background-color: #fff;
      font-family: Arial, sans-serif;
    }
    .tool-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border: 1px solid #ddd;
      border-radius: 6px;
      padding: 1rem;
      background-color: #fafafa;
    }
    button {
      padding: 0.5rem 1rem;
      background-color: #2684FF;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #0f66cc;
    }
  </style>
  
  <main>
    <h1>Tools</h1>
    <!-- Single tool row for the Crawler -->
    <div class="tool-row">
      <div>Crawler</div>
      <button on:click={runCrawler}>Run Crawler</button>
    </div>
  </main>
  