#ifndef BLOCKNOTE_NETWORK_STATUSCODE_HH
#define BLOCKNOTE_NETWORK_STATUSCODE_HH

#include <string>
#include <vector>

namespace blocknote {
namespace network {

enum class status_code {
  unknown = 0,
  information_continue = 100,
  information_switching_protocols,
  information_processing,
  success_ok = 200,
  success_created,
  success_accepted,
  success_non_authoritative_information,
  success_no_content,
  success_reset_content,
  success_partial_content,
  success_multi_status,
  success_already_reported,
  success_im_used = 226,
  redirection_multiple_choices = 300,
  redirection_moved_permanently,
  redirection_found,
  redirection_see_other,
  redirection_not_modified,
  redirection_use_proxy,
  redirection_switch_proxy,
  redirection_temporary_redirect,
  redirection_permanent_redirect,
  client_error_bad_request = 400,
  client_error_unauthorized,
  client_error_payment_required,
  client_error_forbidden,
  client_error_not_found,
  client_error_method_not_allowed,
  client_error_not_acceptable,
  client_error_proxy_authentication_required,
  client_error_request_timeout,
  client_error_conflict,
  client_error_gone,
  client_error_length_required,
  client_error_precondition_failed,
  client_error_payload_too_large,
  client_error_uri_too_long,
  client_error_unsupported_media_type,
  client_error_range_not_satisfiable,
  client_error_expectation_failed,
  client_error_im_a_teapot,
  client_error_misdirection_required = 421,
  client_error_unprocessable_entity,
  client_error_locked,
  client_error_failed_dependency,
  client_error_upgrade_required = 426,
  client_error_precondition_required = 428,
  client_error_too_many_requests,
  client_error_request_header_fields_too_large = 431,
  client_error_unavailable_for_legal_reasons = 451,
  server_error_internal_server_error = 500,
  server_error_not_implemented,
  server_error_bad_gateway,
  server_error_service_unavailable,
  server_error_gateway_timeout,
  server_error_http_version_not_supported,
  server_error_variant_also_negotiates,
  server_error_insufficient_storage,
  server_error_loop_detected,
  server_error_not_extended = 510,
  server_error_network_authentication_required
};

const static std::vector<std::pair<status_code, std::string>>
    &status_codes() noexcept {
  const static std::vector<std::pair<status_code, std::string>> status_codes = {
      {status_code::unknown, ""},
      {status_code::information_continue, "100 Continue"},
      {status_code::information_switching_protocols, "101 Switching Protocols"},
      {status_code::information_processing, "102 Processing"},
      {status_code::success_ok, "200 OK"},
      {status_code::success_created, "201 Created"},
      {status_code::success_accepted, "202 Accepted"},
      {status_code::success_non_authoritative_information,
       "203 Non-Authoritative Information"},
      {status_code::success_no_content, "204 No Content"},
      {status_code::success_reset_content, "205 Reset Content"},
      {status_code::success_partial_content, "206 Partial Content"},
      {status_code::success_multi_status, "207 Multi-Status"},
      {status_code::success_already_reported, "208 Already Reported"},
      {status_code::success_im_used, "226 IM Used"},
      {status_code::redirection_multiple_choices, "300 Multiple Choices"},
      {status_code::redirection_moved_permanently, "301 Moved Permanently"},
      {status_code::redirection_found, "302 Found"},
      {status_code::redirection_see_other, "303 See Other"},
      {status_code::redirection_not_modified, "304 Not Modified"},
      {status_code::redirection_use_proxy, "305 Use Proxy"},
      {status_code::redirection_switch_proxy, "306 Switch Proxy"},
      {status_code::redirection_temporary_redirect, "307 Temporary Redirect"},
      {status_code::redirection_permanent_redirect, "308 Permanent Redirect"},
      {status_code::client_error_bad_request, "400 Bad Request"},
      {status_code::client_error_unauthorized, "401 Unauthorized"},
      {status_code::client_error_payment_required, "402 Payment Required"},
      {status_code::client_error_forbidden, "403 Forbidden"},
      {status_code::client_error_not_found, "404 Not Found"},
      {status_code::client_error_method_not_allowed, "405 Method Not Allowed"},
      {status_code::client_error_not_acceptable, "406 Not Acceptable"},
      {status_code::client_error_proxy_authentication_required,
       "407 Proxy Authentication Required"},
      {status_code::client_error_request_timeout, "408 Request Timeout"},
      {status_code::client_error_conflict, "409 Conflict"},
      {status_code::client_error_gone, "410 Gone"},
      {status_code::client_error_length_required, "411 Length Required"},
      {status_code::client_error_precondition_failed,
       "412 Precondition Failed"},
      {status_code::client_error_payload_too_large, "413 Payload Too Large"},
      {status_code::client_error_uri_too_long, "414 URI Too Long"},
      {status_code::client_error_unsupported_media_type,
       "415 Unsupported Media Type"},
      {status_code::client_error_range_not_satisfiable,
       "416 Range Not Satisfiable"},
      {status_code::client_error_expectation_failed, "417 Expectation Failed"},
      {status_code::client_error_im_a_teapot, "418 I'm a teapot"},
      {status_code::client_error_misdirection_required,
       "421 Misdirected Request"},
      {status_code::client_error_unprocessable_entity,
       "422 Unprocessable Entity"},
      {status_code::client_error_locked, "423 Locked"},
      {status_code::client_error_failed_dependency, "424 Failed Dependency"},
      {status_code::client_error_upgrade_required, "426 Upgrade Required"},
      {status_code::client_error_precondition_required,
       "428 Precondition Required"},
      {status_code::client_error_too_many_requests, "429 Too Many Requests"},
      {status_code::client_error_request_header_fields_too_large,
       "431 Request Header Fields Too Large"},
      {status_code::client_error_unavailable_for_legal_reasons,
       "451 Unavailable For Legal Reasons"},
      {status_code::server_error_internal_server_error,
       "500 Internal Server Error"},
      {status_code::server_error_not_implemented, "501 Not Implemented"},
      {status_code::server_error_bad_gateway, "502 Bad Gateway"},
      {status_code::server_error_service_unavailable,
       "503 Service Unavailable"},
      {status_code::server_error_gateway_timeout, "504 Gateway Timeout"},
      {status_code::server_error_http_version_not_supported,
       "505 HTTP Version Not Supported"},
      {status_code::server_error_variant_also_negotiates,
       "506 Variant Also Negotiates"},
      {status_code::server_error_insufficient_storage,
       "507 Insufficient Storage"},
      {status_code::server_error_loop_detected, "508 Loop Detected"},
      {status_code::server_error_not_extended, "510 Not Extended"},
      {status_code::server_error_network_authentication_required,
       "511 Network Authentication Required"}};
  return status_codes;
}

inline status_code status_code(const std::string &status_code_str) noexcept {
  for (auto &status_code : status_codes()) {
    if (status_code.second == status_code_str) return status_code.first;
  }
  return status_code::unknown;
}

inline const std::string &status_code(enum status_code status_code_enum) noexcept {
  for (auto &status_code : status_codes()) {
    if (status_code.first == status_code_enum) return status_code.second;
  }
  return status_codes()[0].second;
}
}  // namespace network
}  // namespace blocknote

#endif  // BLOCKNOTE_NETWORK_STATUSCODE_HH