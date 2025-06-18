$(document).ready(function () {
  $("#table_id").DataTable({
    paging: false,
    ordering: false,
    info: false,
    responsive: true,
  });
  $("#table_id2").DataTable({
    paging: false,
    ordering: false,
    info: false,
    responsive: true,
    searching: false,
  });
});
