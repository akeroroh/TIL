<template>
    <main class="container py-3">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
        <div class="col" v-for="_ in numberOfItems">
            <GalleryListItem />
        </div>
        </div>
    </main>
</template>

<script setup>
    const numberOfItems = 4
    import GalleryListItem from '@/components/GalleryListItem.vue'
</script>
