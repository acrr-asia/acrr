# Vietnamese translation guide

ACRR is published in English (the original) and Vietnamese (translations). This file is the
contract for every Vietnamese translation: where files go, what must stay identical to the
English original, and how technical terms are written. It is for authors and translators, not
for visitors.

## Files

| Content | English original | Vietnamese translation | Public URL |
|---|---|---|---|
| Article | `src/content/blog/<slug>.mdx` | `src/content/blog/vi/<slug>.mdx` | `/vi/blog/<slug>` |
| Series | `src/content/series/<id>.md` | `src/content/series/vi/<id>.md` | `/vi/series/<id>` |
| Insight | `src/content/insights/<id>.md` | `src/content/insights/vi/<id>.md` | `/vi/insights/<id>` |
| Learning item | `src/data/learning.json` | the item's optional `vi` object in the same file | `/vi/learning` |
| Interface text | `src/i18n/ui.ts` (`en`) | `src/i18n/ui.ts` (`vi`) | every `/vi/...` page |

A translation has the same file name (slug or id) as its original; the build fails if a
translation has no original. An untranslated article or insight still appears in Vietnamese
listings, marked as English and linking to the English page.

## What stays identical to the original

Frontmatter, except `title` and `description` (and, for a series, `objectives` and the titles and
descriptions of `plannedEntries`), is copied unchanged: `publishedAt`, `updatedAt`, `category`,
`tags`, `series`, `seriesOrder`, `status`, `kind`, `draft`, `example`. A series translation must
list the same number of planned entries, in the same order, and have the same `status` as the
original (the build checks both), so when an English series file changes, its translation must
change with it.

Also unchanged: every formula and number, code blocks, units and their symbols, figure
components and their props other than `caption`, reference lists (titles of cited works stay in
their original language), and the structure (same sections, same numbering, same tables).

In an `.mdx` translation, imports point one directory further up:
`import Figure from '../../../components/Figure.astro';`.

Links to another article point to its Vietnamese version (`/vi/blog/<slug>`) only when that
translation exists; otherwise they keep the English URL. Do not link to in-page anchors of a
translated page: Vietnamese headings produce different anchors from the English ones.

Mermaid diagrams are translated (node and edge labels); the generated SVG diagrams in
`src/components/diagrams/` keep their English labels for now, and their Vietnamese captions say
what the figure shows.

## Style

- Natural, precise technical Vietnamese, as in a good Vietnamese university textbook; not a
  word-for-word rendering of the English sentence structure. Keep the meaning, the order of ideas
  and every technical claim exactly.
- **Terms:** on its first use in each article, write the Vietnamese term followed by the English
  term in parentheses, for example *cầu Wheatstone (Wheatstone bridge)*, *độ không đảm bảo đo
  (measurement uncertainty)*; afterwards use the Vietnamese term alone. Keep standard acronyms as
  they are (ADC, DAC, SAR, CMRR, JWT, OAuth, HTTP, TLS, PID) and expand them in Vietnamese on first
  use, for example *bộ chuyển đổi tương tự – số (analog-to-digital converter, ADC)*. Where no
  established Vietnamese term exists, keep the English term in italics.
- **Numbers:** keep the decimal point used in the original (`0.385 Ω/°C`, `2.5 mV`) so prose,
  tables and formulas agree; separate thousands with a thin space as the original does
  (`65 536`). Units and symbols follow SI and are not translated.
- Section labels in summaries and tables are translated; table structure is unchanged.
- "Entry" (a part of a series) is *bài*; "the previous entry" is *bài trước*, "the next entry"
  *bài tiếp theo*, "the first entry" *bài thứ nhất*.

## Glossary

Use these renderings so that terms agree across articles.

| English | Tiếng Việt |
|---|---|
| measurement, measurand | phép đo, đại lượng cần đo |
| sensor, transducer | cảm biến, bộ chuyển đổi |
| measurement chain | chuỗi đo |
| sensing element | phần tử cảm biến |
| signal conditioning | chuẩn hóa tín hiệu (signal conditioning) |
| modulating / self-generating sensor | cảm biến điều chế / cảm biến tự phát |
| excitation | nguồn kích thích |
| sensitivity, resolution, accuracy, precision | độ nhạy, độ phân giải, độ chính xác, độ chụm |
| linearity, nonlinearity | độ tuyến tính, độ phi tuyến |
| hysteresis, drift, repeatability | độ trễ (hysteresis), độ trôi, độ lặp lại |
| range, span, full scale | dải đo, khoảng đo, toàn thang |
| error (systematic / random) | sai số (hệ thống / ngẫu nhiên) |
| uncertainty (standard / combined / expanded) | độ không đảm bảo đo (chuẩn / tổng hợp / mở rộng) |
| coverage factor | hệ số phủ |
| calibration, traceability | hiệu chuẩn, tính liên kết chuẩn |
| influence quantity | đại lượng ảnh hưởng |
| loading (effect) | hiệu ứng tải |
| time constant, bandwidth, cut-off frequency | hằng số thời gian, băng thông, tần số cắt |
| step response, frequency response | đáp ứng bước, đáp ứng tần số |
| strain gauge, gauge factor | cảm biến biến dạng (strain gauge), hệ số gauge |
| thermocouple, cold junction | cặp nhiệt điện, mối nối lạnh |
| resistance thermometer (PT100) | nhiệt điện trở bạch kim (PT100) |
| thermistor | nhiệt điện trở bán dẫn (thermistor) |
| photodiode, responsivity | điốt quang, độ đáp ứng |
| Wheatstone bridge, quarter / half / full bridge | cầu Wheatstone, cầu một phần tư / nửa cầu / cầu đủ |
| operational amplifier (op-amp) | bộ khuếch đại thuật toán (op-amp) |
| instrumentation amplifier | bộ khuếch đại đo lường (instrumentation amplifier) |
| common-mode / differential-mode | chế độ chung / chế độ vi sai |
| common-mode rejection ratio (CMRR) | tỉ số nén tín hiệu đồng pha (CMRR) |
| virtual ground | đất ảo |
| transimpedance amplifier | bộ khuếch đại xuyên trở (transimpedance amplifier) |
| charge amplifier | bộ khuếch đại điện tích |
| gain–bandwidth product | tích độ lợi – băng thông |
| offset voltage, bias current | điện áp lệch, dòng phân cực |
| low-pass filter, order | bộ lọc thông thấp, bậc |
| sampling, sampling frequency | lấy mẫu, tần số lấy mẫu |
| aliasing, alias, anti-aliasing filter | chồng phổ (aliasing), thành phần chồng phổ, bộ lọc chống chồng phổ |
| Nyquist frequency, sampling theorem | tần số Nyquist, định lý lấy mẫu |
| quantization, quantization step, LSB | lượng tử hóa, bước lượng tử, LSB |
| analog-to-digital converter (ADC) | bộ chuyển đổi tương tự – số (ADC) |
| digital-to-analog converter (DAC) | bộ chuyển đổi số – tương tự (DAC) |
| successive approximation, delta-sigma | xấp xỉ liên tiếp, delta-sigma |
| oversampling, decimation | lấy mẫu vượt mức, giảm tốc độ mẫu (decimation) |
| noise (thermal, shot, flicker), interference | nhiễu (nhiệt, bắn, nhấp nháy 1/f), can nhiễu |
| robot, degree of freedom | robot, bậc tự do |
| coordinate frame, transformation | hệ tọa độ, phép biến đổi |
| forward / inverse kinematics | động học thuận / động học ngược |
| state estimation, Kalman filter | ước lượng trạng thái, bộ lọc Kalman |
| feedback, controller, plant | phản hồi, bộ điều khiển, đối tượng điều khiển |
| authentication, authorization | xác thực, phân quyền |
| token, session, cookie | token, phiên, cookie |
| load cell | cảm biến lực (load cell) |
| voltage divider | mạch phân áp |
| dummy gauge | cảm biến biến dạng bù (dummy gauge) |
| voltage follower (buffer) | mạch lặp điện áp (mạch đệm) |
| difference / differential amplifier | bộ khuếch đại hiệu / bộ khuếch đại vi sai |
| ratiometric (measurement) | phép đo tỉ lệ (ratiometric) |
| notch filter, active filter | bộ lọc chắn dải hẹp (notch filter), bộ lọc tích cực |
| synchronous demodulator | bộ giải điều chế đồng bộ |
| galvanic isolation | cách ly galvanic |
| magnitude response | đáp ứng biên độ |
| energy domain | miền năng lượng |
| dark current, quantum efficiency | dòng tối, hiệu suất lượng tử |
| eddy current, magnetoresistive | dòng xoáy, từ trở |
| trueness, cross-sensitivity | độ đúng, độ nhạy chéo |
| threshold, dead band | ngưỡng, vùng chết |
| damping ratio, natural frequency | hệ số tắt dần, tần số dao động riêng |
| actuator | cơ cấu chấp hành |
| noise shaping, zero-order hold | định dạng nhiễu, giữ bậc không |
| reconstruction filter | bộ lọc khôi phục |
| offset error, gain error, missing code | sai số lệch không, sai số độ lợi, mã bị thiếu |
| aperture jitter | độ rung pha khẩu độ (aperture jitter) |
| dither | dither (kept in English) |
| digital twin, fieldbus | bản sao số, bus trường |
| verification, validation | kiểm chứng, thẩm định |
