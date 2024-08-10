<template>
  <div class="home">
    <DeleteProduct msg="Delete Product"/>
  </div>
</template>

<script>
// @ is an alias to /src
import DeleteProduct from '@/components/DeleteProduct.vue'

export default {
  name: 'DeleteProductView',
  components: {
    DeleteProduct
  }
}
</script>
