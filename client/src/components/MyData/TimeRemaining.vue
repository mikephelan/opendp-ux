<template>
   <span
       :class="{
            'error_status__color--text': timeRemaining === 'Expired'
          }"
   >{{ timeRemaining }}</span
   >


</template>

<script>


export default {
  name: "TimeRemaining",
  created() {
    console.log("creating component")
  },
  mounted: function () {
    console.log('mounted', this.item)
  },

  computed: {
    timeRemaining: function () {
      console.log('in computed createdTime=' + this.createdTime)
      const maxHours = 36
      const now = new Date().getTime();
      console.log('now=' + new Date())
      console.log('now time=' + new Date().getTime())
      const createdMillis = Date.parse(this.createdTime)
      const diffInSeconds = (now - createdMillis) / 1000;
      // calculate hours
      const hours = Math.floor(diffInSeconds / 3600);
      console.log('hours ' + hours)
      const hoursRemaining = maxHours - hours
      console.log('calculated hours', hoursRemaining);
      if (hoursRemaining > 0) {
        return hoursRemaining + 'hrs'
      } else {
        return 'Expired'
      }
    }
  },
  props: ["createdTime"]
};
</script>
