$.ajax({
    type : 'POST',
    url : "edit",
    data : {
        item_id: id
    },
    success: function(data){
        document.getElementById('search').value = data.itemval
    }
})