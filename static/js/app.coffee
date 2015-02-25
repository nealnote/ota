$('.J_list').eq(0).addClass('active')
$('.J_device h3').on 'click', ->
  trigger = $(this)
  holder = $(this).next()
  current = trigger.siblings('.active').prev()
  if trigger.is(current)
    holder.removeClass('active')
    return false
  trigger.siblings('.J_list').removeClass('active')
  holder.addClass('active')