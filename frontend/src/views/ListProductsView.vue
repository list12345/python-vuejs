<template>
  <div class="home">
    <ListProduct msg="List Product"/>
  </div>
</template>

<script>
// @ is an alias to /src
import ListProduct from '@/components/ListProduct.vue'

export default {
  name: 'ListProductsView',
  components: {
    ListProduct
  }
}
</script>
