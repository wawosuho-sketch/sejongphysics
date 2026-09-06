<script>
  import { onMount } from "svelte";
  import Home from "./lib/pages/Home.svelte";
  import LecturePage from "./lib/pages/LecturePage.svelte";
  import DrawingToolbar from "./lib/components/DrawingToolbar.svelte";
  import { textbooks } from "./lib/data/textbooks.js";

  let currentRoute = "home";
  let targetSlide = 1;
  let activeBookId = "physics";

  function syncFromUrl() {
    const params = new URLSearchParams(window.location.search);
    const page = params.get("page");
    const bookParam = params.get("book");
    const savedBook = localStorage.getItem("selectedBookId");

    if (bookParam && textbooks.some((b) => b.id === bookParam)) {
      activeBookId = bookParam;
      localStorage.setItem("selectedBookId", bookParam);
    } else if (savedBook && textbooks.some((b) => b.id === savedBook)) {
      activeBookId = savedBook;
    }

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

  function navigate(route, slide = 1, bookId = null) {
    currentRoute = route;
    targetSlide = slide;

    if (bookId && textbooks.some((b) => b.id === bookId)) {
      activeBookId = bookId;
      localStorage.setItem("selectedBookId", bookId);
    }

    const url = new URL(window.location.href);
    if (route === "home") {
      url.searchParams.delete("page");
      url.searchParams.delete("slide");
      url.searchParams.set("book", activeBookId);
      window.scrollTo({ top: 0, behavior: "smooth" });
    } else {
      url.searchParams.set("page", route);
      url.searchParams.set("book", activeBookId);
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
  <Home {navigate} initialBookId={activeBookId} />
{:else if currentRoute.startsWith("lecture_")}
  <LecturePage
    lectureId={currentRoute.replace("lecture_", "")}
    {navigate}
    initialSlide={targetSlide}
  />
{/if}

<DrawingToolbar />
