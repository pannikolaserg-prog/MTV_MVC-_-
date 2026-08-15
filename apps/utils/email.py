# utils/email.py


def send_email_notification(user, entry):
    """Отправляет уведомление на email (через консоль для демонстрации)"""
    message = f"""
    ═══════════════════════════════════════════════
    📧 НОВАЯ ЗАПИСЬ В ДНЕВНИКЕ
    ═══════════════════════════════════════════════

    👤 Пользователь: {user.username} ({user.email})
    📌 Заголовок: {entry.title}
    📅 Создано: {entry.created_at.strftime('%d.%m.%Y %H:%M')}

    📖 Содержание:
    {entry.content}

    🏷️ Теги: {', '.join(entry.tags) if entry.tags else 'нет'}
    🔓 Публичная: {'Да' if entry.is_public else 'Нет'}

    ═══════════════════════════════════════════════
    ✅ Уведомление отправлено
    """
    print(message)
    return True
