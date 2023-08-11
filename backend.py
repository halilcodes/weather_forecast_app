import requests

API_key = "656f85f3adc9af01b884b38aba53a60c"


def get_data(location, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_key}"
    length = int(forecast_days) * 8
    response = requests.get(url)
    content = response.json()
    content = content["list"][:length]

    d_dt, d_text, t, sky, data = [], [], [], [], {}
    for each in content:
        # d_dt.append(each['dt'])
        d_text.append(each['dt_txt'])
        t.append(each['main']['temp']/10)
        sky.append(each['weather'][0]['main'].lower())
        # data[each['dt_txt']] = {"d_dt": each['dt'],
        #                         "temp": each['main']['temp'],
        #                         "sky": each['weather'][0]['main'].lower()}

    return sky, t, d_text


if __name__ == "__main__":
    print(get_data("tokyo", 3))
