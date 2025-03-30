<script>
  import { onMount } from 'svelte';
  import { select, hierarchy, tree, linkVertical } from 'd3';

  // Expects "data" to be an array of top-level items:
  // [
  //   {
  //     name: '192.168.1.25:8080',
  //     children: [
  //       { name: '/quests/success-stories', children: [...] },
  //       { name: '/quests/shareform', children: [...] }
  //     ]
  //   },
  //   {
  //     name: 'discord.com',
  //     children: []
  //   }
  // ]
  export let data = [];

  let width = 800;
  let height = 500;
  let container; // Bind the <div> to this variable

  
  onMount(() => {
    // 1) Wrap the user data in a fake root (for multiple top-level nodes)
    const fakeRoot = { name: 'ROOT', children: data };

    // 2) Build a D3 hierarchy
    const root = hierarchy(fakeRoot);

    // 3) Create a tree layout with size [width, height]
    //    For top-to-bottom, x is horizontal and y is vertical.
    const layout = tree().size([width, height - 100]);
    layout(root);

    // 4) Append an <svg> into the container
    const svg = select(container)
      .append('svg')
      .attr('width', width)
      .attr('height', height);

    // 5) Draw the links (paths) using linkVertical
    svg.selectAll('.link')
      .data(root.links())
      .enter()
      .append('path')
      .attr('class', 'link')
      .attr('d', linkVertical()
        .x(d => d.x)
        .y(d => d.y)
      );

    // 6) Draw the nodes
    const node = svg.selectAll('.node')
      .data(root.descendants())
      .enter()
      .append('g')
      .attr('class', 'node')
      // Position each node at (d.x, d.y)
      .attr('transform', d => `translate(${d.x},${d.y})`);

    // 7) For each node, draw a rectangle (light gray, no border)
    node.append('rect')
      .attr('width', 120)
      .attr('height', 60)
      .attr('x', -60)  // center horizontally
      .attr('y', -15)  // center vertically
      .attr('rx', 5)   // rounded corners
      .attr('ry', 5)
      .attr('fill', '#d3d3d3') // light gray fill
      .attr('stroke', 'none'); // no border

    // 8) For each node, add text
    node.append('text')
      .attr('dy', '0.35em')
      .attr('text-anchor', 'middle')
      .text(d => d.data.name);
  });
</script>

<!-- The tree graph will render inside this container -->
<div bind:this={container} />

<style>
  /* Style the links connecting nodes */
  :global(.link) {
    fill: none;
    stroke: #4ea8b2;
    stroke-width: 2;
  }


  /* Style for node text */
  :global(.node text) {
    font-size: 14px;
    font-weight: bold;
    fill: #333;
    text-anchor: middle;
  }

  /* Optional container spacing */
  div {
    margin: 1rem 0;
  }
</style>
