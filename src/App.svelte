<script>
  import { onMount } from "svelte";
  import Home from "./lib/pages/Home.svelte";
  import LecturePage from "./lib/pages/LecturePage.svelte";
  import DrawingToolbar from "./lib/components/DrawingToolbar.svelte";

  let currentRoute = "home";
  let targetSlide = 1;

  function syncFromUrl() {
    const params = new URLSearchParams(window.location.search);
    const page = params.get("page");
    if (page) {
      currentRoute = page;
      targetSlide = parseInt(params.get("slide") || "1", 10);
    } else {
      currentRoute = "home";
      targetSlide = 1;
    }
  }

  onMount(() => {
    syncFromUrl(); // Initialize on load
    window.addEventListener("popstate", syncFromUrl);
    return () => window.removeEventListener("popstate", syncFromUrl);
  });

  function navigate(route, slide = 1) {
    currentRoute = route;
    targetSlide = slide;

    const url = new URL(window.location.href);
    if (route === "home") {
      url.search = "";
      window.scrollTo({ top: 0, behavior: "smooth" });
    } else {
      url.searchParams.set("page", route);
      if (slide > 1) {
        url.searchParams.set("slide", slide.toString());
      } else {
        url.searchParams.delete("slide");
      }
    }
    window.history.pushState({}, "", url);
  }
</script>

{#if currentRoute === "home"}
  <Home {navigate} />
{:else if currentRoute.startsWith("lecture_")}
  <LecturePage
    lectureId={currentRoute.replace("lecture_", "")}
    {navigate}
    initialSlide={targetSlide}
  />
{/if}

<DrawingToolbar />
