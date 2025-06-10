# 라이브러리 설치 후 실행하세요
import folium

# 서울 중심 좌표 (서울시청 기준)
seoul_center = [37.5665, 126.9780]

# folium을 이용한 지도 생성
map_seoul = folium.Map(location=seoul_center, zoom_start=12)

# 샘플 편의점 위치 데이터 (추후 실제 데이터로 교체 가능)
convenience_stores = [
    {'name': 'GS25 서울역점', 'brand': 'GS25', 'lat': 37.5547, 'lon': 126.9706},
    {'name': 'GS25 강남점', 'brand': 'GS25', 'lat': 37.4979, 'lon': 127.0276},
    
    {'name': '세븐일레븐 홍대점', 'brand': 'SevenEleven', 'lat': 37.5563, 'lon': 126.9236},
    {'name': '세븐일레븐 종로점', 'brand': 'SevenEleven', 'lat': 37.5720, 'lon': 126.9817},
    
    {'name': 'CU 신촌점', 'brand': 'CU', 'lat': 37.5585, 'lon': 126.9371},
    {'name': 'CU 강동구청점', 'brand': 'CU', 'lat': 37.5302, 'lon': 127.1238}
]

# 편의점 브랜드별 색상 지정
brand_colors = {
    'GS25': 'blue',
    'SevenEleven': 'green',
    'CU': 'purple'
}

# 각 편의점 위치에 마커 표시
for store in convenience_stores:
    folium.Marker(
        location=[store['lat'], store['lon']],
        popup=f"{store['brand']} - {store['name']}",
        icon=folium.Icon(color=brand_colors[store['brand']])
    ).add_to(map_seoul)

# 지도 결과를 HTML 파일로 저장
map_seoul.save('seoul_convenience_stores.html')

print("지도 생성 완료: 'seoul_convenience_stores.html' 파일을 열어보세요.")
