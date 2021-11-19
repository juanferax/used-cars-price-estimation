<template lang="html">
    <div class="body">
        <div class="text-5xl bg-blue-500"> Hola mundo </div>
        <div class="bg-purple-500 text-white"> Test </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Main',
    data() {
        return {
            message: 'Home Page'
        }
    },
    methods: {
        getMessage() {
            const path = 'http://localhost:5000/api/v1.0/message'
            axios.get(path).then((response)  => {
                this.message = response.data
            })
            .catch((error) => {
                 console.error(error)
            })
        }
    },
    created() {
        this.getMessage()
    }
}
</script>