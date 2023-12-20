def solution(data, ext, val_ext, sort_by):
    sort_dict = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    sort_key = sort_dict[ext]
    data = [dt for dt in data if dt[sort_key] < val_ext]
    sorted_data = sorted(data, key=lambda x: x[sort_dict[sort_by]])

    return sorted_data


if __name__ == "__main__":
    print(
        solution(
            [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],
            "date",
            20300501,
            "remain",
        )
    )