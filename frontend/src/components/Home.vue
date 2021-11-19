<template lang="html">
    <div class="body">
        <h1> {{ message }} </h1>
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