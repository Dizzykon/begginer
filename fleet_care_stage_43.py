# === Stage 43: Добавь пагинацию длинных списков ===
# Project: FleetCare
def paginate(items: list, page_size: int = 20, current_page: int = 1) -> dict:
    """Compact pagination helper: returns {page, page_size, total, total_pages, items, prev, next}."""
    if page_size <= 0 or current_page < 1:
        raise ValueError("page_size must be > 0 and current_page must be >= 1")
    total = len(items)
    total_pages = max(1, (total + page_size - 1) // page_size)
    start = (current_page - 1) * page_size
    end = start + page_size
    page_items = items[start:end]
    return {
        "page": current_page,
        "page_size": page_size,
        "total": total,
        "total_pages": total_pages,
        "items": page_items,
        "prev": current_page - 1 if current_page > 1 else None,
        "next": current_page + 1 if current_page < total_pages else None,
    }
