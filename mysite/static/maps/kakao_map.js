var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };


$('#searchBtn').click(function () {
    // 버튼을 click했을때

    // 지도를 생성합니다
    var map = new kakao.maps.Map(mapContainer, mapOption);

    // 주소-좌표 변환 객체를 생성합니다
    var geocoder = new kakao.maps.services.Geocoder();

    // 주소로 좌표를 검색합니다
    geocoder.addressSearch($('#area').val(), function (result, status) {

        // 정상적으로 검색이 완료됐으면
        if (status === kakao.maps.services.Status.OK) {
            var coords = new kakao.maps.LatLng(result[0].y, result[0].x);

            // 추출한 좌표를 통해 도로명 주소 추출
            let lat = result[0].y;
            let lng = result[0].x;
            getAddr(lat, lng);

            function getAddr(lat, lng) {
                let geocoder = new kakao.maps.services.Geocoder();

                let coord = new kakao.maps.LatLng(lat, lng);
                let callback = function (result, status) {
                    if (status === kakao.maps.services.Status.OK) {
                        // 추출한 도로명 주소를 해당 input의 value값으로 적용
                        $('#area').val(result[0].road_address.address_name);
                    }
                }
                geocoder.coord2Address(coord.getLng(), coord.getLat(), callback);
            }

            // 결과값으로 받은 위치를 마커로 표시합니다
            var marker = new kakao.maps.Marker({
                map: map,
                position: coords
            });


            // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
            map.setCenter(coords);
        }
    });
});
